import React from "react";
import {useParams} from "react-router-dom";


const TodoItem = ({item}) => {

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
                {item.is_active}
            </td>
        </tr>
    )
}

const ProjectTodoList = ({items}) => {

    let {projectId} = useParams()
    let filteredItems = items.filter((item) => item.project == projectId)

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

            {filteredItems.map((item) => <TodoItem item = {item}/>)}
        </table>
    )
}

export default ProjectTodoList;