import threading

from copy import deepcopy
from savraska.utils import Subject

from savraska.exceptions import RecordNotFoundException, DbCommitException, DbDeleteException, DbUpdateException
from sqlite3 import connect


connection = connect('database.sqlite', check_same_thread=False)


class UnitOfWork(threading.local):

    current = None
    mr = None

    def __init__(self):
        super(UnitOfWork, self).__init__()

        self.new_objects = []
        self.dirty_objects = []
        self.del_objects = []

    def register_new(self, obj):
        self.new_objects.append(obj)

    def register_dirty(self, obj):
        self.dirty_objects.append(obj)

    def register_del(self, obj):
        self.del_objects.append(obj)

    def insert(self):
        for elem in self.new_objects:
            self.mr.get_mapper(elem).insert(elem)

    def update(self):
        for elem in self.dirty_objects:
            self.mr.get_mapper(elem).update(elem)

    def delete(self):
        for elem in self.del_objects:
            self.mr.get_mapper(elem).delete(elem)

    def commit(self):
        self.insert()
        self.update()
        self.delete()

        self.new_objects.clear()
        self.dirty_objects.clear()
        self.del_objects.clear()

    @classmethod
    def set_mapper_registry(cls, MapperRegistry):
        cls.mr = MapperRegistry

    @classmethod
    def new_current(cls):
        cls.current = UnitOfWork()

    @classmethod
    def get_current(cls):
        return cls.current


class DomainObject:

    def mark_new(self):
        UnitOfWork.get_current().register_new(self)

    def mark_update(self):
        UnitOfWork.get_current().register_dirty(self)

    def mark_delete(self):
        UnitOfWork.get_current().register_del(self)


# region Users

class User:
    def __init__(self, id, name: str):
        self.id = id
        self.name = name


class Teacher(User):
    pass


class Student(User, DomainObject):
    def __init__(self, id, name: str):
        super(Student, self).__init__(id, name)

# endregion


# region Courses

class CoursePrototype:
    """ Паттерн прототип """

    def clone(self):
        return deepcopy(self)


class Course(CoursePrototype, Subject, DomainObject):

    def __init__(self, id, id_category, name):
        self.id = id
        self.id_category = id_category
        self.name = name

        super(Course, self).__init__()

    def add_student_event(self):
        self.notify()


class InteractiveCourse(Course):
    pass


class RecordCourse(Course):
    pass


class CourseStudent(DomainObject):
    def __init__(self, id_student, id_course):
        self.id_student = id_student
        self.id_course = id_course

# endregion


class Category(DomainObject):

    def __init__(self, id, parent_category_id,  name):
        self.id = id
        self.name = name
        self.categories = []

    def __str__(self):
        return f'{self.name}: {self.id}'


class BaseMapper:
    """ Базовый маппер """

    def __init__(self, connection):
        self.connection = connection
        self.cursor = connection.cursor()
        self.tablename = 'some_table'

    def all(self):
        pass

    def get(self, id):
        pass

    def insert(self, obj):
        statement = f'INSERT INTO {self.tablename} (name) VALUES (?)'
        self.cursor.execute(statement, (obj.name,))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbCommitException(e.args)

    def update(self, obj):
        statement = f'UPDATE {self.tablename} SET name=? WHERE id=?'

        self.cursor.execute(statement, (obj.id, obj.name))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbUpdateException(e.args)

    def delete(self, obj):
        statement = f'DELETE FROM {self.tablename} WHERE id=?'
        self.cursor.execute(statement, (obj.id,))
        try:
            self.connection.commit()
        except Exception as e:
            raise DbDeleteException(e.args)


class CourseStudentMapper(BaseMapper):
    """ Маппер записей на курс """

    def __init__(self, connection):
        super(CourseStudentMapper, self).__init__(connection)
        self.tablename = 'students_courses'

    def insert(self, obj):
        statement = f'INSERT INTO {self.tablename} (id_student, id_course) VALUES (?, ?)'
        self.cursor.execute(statement, (obj.id_student, obj.id_course))

        try:
            self.connection.commit()
        except Exception as e:
            raise DbCommitException(e.args)

class CourseMapper(BaseMapper):
    """ Маппер курсов """

    def __init__(self, connection):
        super(CourseMapper, self).__init__(connection)
        self.tablename = 'courses'

    def all(self):
        statement = f'SELECT * from {self.tablename}'
        self.cursor.execute(statement)
        result = []
        for item in self.cursor.fetchall():
            id, id_category, name = item

            course = Course(0, id_category, name)
            course.id = id
            result.append(course)

        return result

    def get_by_category_id(self, category_id):
        statement = f'SELECT * from {self.tablename} WHERE id_category=?'
        self.cursor.execute(statement, (category_id,))
        result = []
        for item in self.cursor.fetchall():
            id, id_category, name = item

            course = Course(0, id_category, name)
            course.id = id
            result.append(course)

        return result

    def get(self, id):
        statement = f'SELECT id, id_category, name FROM {self.tablename} WHERE id=?'
        self.cursor.execute(statement, (id,))
        result = self.cursor.fetchone()

        if result:
            return Course(*result)
        else:
            raise RecordNotFoundException(f'record with id={id} not found')

    def insert(self, obj):
        statement = f'INSERT INTO {self.tablename} (id_category, name) VALUES (?, ?)'
        self.cursor.execute(statement, (obj.id_category, obj.name))

        try:
            self.connection.commit()
        except Exception as e:
            raise DbCommitException(e.args)


class CategoryMapper(BaseMapper):
    """ Маппер категорий """

    def __init__(self, connection):
        super(CategoryMapper, self).__init__(connection)
        self.tablename = 'categories'

    def all(self):
        statement = f'SELECT * from {self.tablename}'
        self.cursor.execute(statement)
        result = []
        for item in self.cursor.fetchall():
            id, parent_id, name = item
            category = Category(id, parent_id, name)
            category.id = id
            result.append(category)

        return result

    def get(self, id):
        statement = f'SELECT id, parent_id, name FROM {self.tablename} WHERE id=?'
        self.cursor.execute(statement, (id,))
        result = self.cursor.fetchone()
        if result:
            return Category(*result)
        else:
            raise RecordNotFoundException(f'record with id={id} not found')


class StudentMapper(BaseMapper):
    """ Маппер студентов """

    def __init__(self, connection):
        super(StudentMapper, self).__init__(connection)
        self.tablename = 'students'

    def all(self):
        statement = f'SELECT * from {self.tablename}'
        self.cursor.execute(statement)
        result = []
        for item in self.cursor.fetchall():
            student = Student(*item)
            result.append(student)

        return result

    def get(self, id):
        statement = f'SELECT id, name FROM {self.tablename} WHERE id=?'
        self.cursor.execute(statement, (id,))
        result = self.cursor.fetchone()
        if result:
            return Student(*result)
        else:
            raise RecordNotFoundException(f'record with id={id} not found')


class MapperRegistry:

    mappers = {
        'student': StudentMapper,
        'category': CategoryMapper,
        'course': CourseMapper,
        'course_student': CourseStudentMapper
    }

    @staticmethod
    def get_mapper(obj):

        if isinstance(obj, Student):

            return StudentMapper(connection)

        if isinstance(obj, Category):

            return CategoryMapper(connection)

        if isinstance(obj, Course):

            return CourseMapper(connection)

        if isinstance(obj, CourseStudent):

            return CourseStudentMapper(connection)

    @staticmethod
    def get_current_mapper(name):
        return MapperRegistry.mappers[name](connection)

#
# unit_of_work = UnitOfWork()
# unit_of_work.new_current()
# unit_of_work.get_current().set_mapper_registry(MapperRegistry)