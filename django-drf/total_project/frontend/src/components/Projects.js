import React from "react";
import {Link} from "react-router-dom";


const ProjectItem = ({item, delete_proc}) => {

    return (
        <tr>
            <td>
                <Link to={`project/${item.id}`}>{item.name}</Link>
            </td>
            <td>
                {item.repo}
            </td>
            <td>
                {item.users}
            </td>
            <th>
                <button onClick={() => delete_proc(item.id)} type='button'>Delete</button>
            </th>
        </tr>
    )

}

const ProjectList = ({items, delete_proc}) => {

    return (
        <table>
            <th>
                Name
            </th>
            <th>
                Repo
            </th>
            <th>
                Users
            </th>
            <th>
                Delete
            </th>
            {items.map((item) => <ProjectItem item={item} delete_proc={delete_proc}/>)}
        </table>
    )
}

export default ProjectList;