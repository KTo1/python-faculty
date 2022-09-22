import graphene
from graphene import ObjectType, Mutation
from graphene_django import DjangoObjectType

from todoapp.models import Project, ToDo
from usersapp.models import User


#region Type

class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'

#endregion

#region ToDo mutation

class ToDoCreateMutation(Mutation):
    class Arguments:
        project_id = graphene.Int()
        user_id = graphene.Int()
        subject = graphene.String()

    todo = graphene.Field(ToDoType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        return cls(todo=ToDo.objects.create(**kwargs))


class ToDoUpdateMutation(Mutation):
    class Arguments:
        id = graphene.ID()
        subject = graphene.String()

    todo = graphene.Field(ToDoType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        todo = ToDo.objects.get(id=kwargs.get('id'))
        todo.subject = kwargs.get('subject')
        todo.save()

        return cls(todo=todo)


class ToDoDeleteMutation(Mutation):
    class Arguments:
        id = graphene.ID()

    todo = graphene.List(ToDoType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        ToDo.objects.get(id=kwargs.get('id')).delete()
        return cls(todo=ToDo.objects.all())

#endregion

#region Project mutation

class ProjectCreateMutation(Mutation):
    class Arguments:
        name = graphene.String()
        repo = graphene.String()
        users = graphene.List(graphene.Int)

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        project = Project()
        project.name = kwargs.get('name')
        project.repo = kwargs.get('repo')
        project.save()

        project.users.set(kwargs.get('users'))
        project.save()

        return cls(project=project)


class ProjectUpdateMutation(Mutation):
    class Arguments:
        id = graphene.ID()
        name = graphene.String()

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        project = Project.objects.get(id=kwargs.get('id'))
        project.name = kwargs.get('name')
        project.save()

        return cls(project=project)


class ProjectDeleteMutation(Mutation):
    class Arguments:
        id = graphene.ID()

    project = graphene.List(ProjectType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        Project.objects.get(id=kwargs.get('id')).delete()
        return cls(project=Project.objects.all())

#endregion

class Mutations(ObjectType):
    create_todo = ToDoCreateMutation.Field()
    update_todo = ToDoUpdateMutation.Field()
    delete_todo = ToDoDeleteMutation.Field()

    create_project = ProjectCreateMutation.Field()
    update_project = ProjectUpdateMutation.Field()
    delete_project = ProjectDeleteMutation.Field()


class Query(ObjectType):
    hello_world = graphene.String(default_value='Hello, World!')

    all_todos = graphene.List(ToDoType)
    all_users = graphene.List(UserType)
    all_projects = graphene.List(ProjectType)

    user_todos = graphene.List(ToDoType, user_id=graphene.Int(required=False))
    user_project = graphene.List(ProjectType, user_id=graphene.Int(required=False))

    def resolve_all_todos(root, info):
        return ToDo.objects.all()

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_user_todos(root, info, user_id=None):
        if user_id:
            return ToDo.objects.filter(user__id=user_id)
        return None

    def resolve_user_project(root, info, user_id=None):
        if user_id:
            return Project.objects.filter(users__id=user_id)
        return None


schema = graphene.Schema(query=Query, mutation=Mutations)