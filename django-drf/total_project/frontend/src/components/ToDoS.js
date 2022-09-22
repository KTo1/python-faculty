import React from "react";


const TodoItem = ({item, delete_proc}) => {

    return (
        <tr>
            <td>
                {item.subject}
            </td>
            <td>
                {item.user}
            </td>
            <td>
                {item.created}
            </td>
            <td>
                {item.is_active.toString() }
            </td>
            <th>
                <button onClick={() => delete_proc(item.id)} type='button'>Delete</button>
            </th>
        </tr>
    )
}

const TodoList = ({items, delete_proc}) => {

    return (
        <table>
            <th>
                Subject
            </th>
            <th>
                User
            </th>
            <th>
                Created
            </th>
            <th>
                Active
            </th>
            <th>
                Delete
            </th>

            {items.map((item) => <TodoItem item = {item} delete_proc={delete_proc}/>)}
        </table>
    )
}

export default TodoList;