import React from "react";
import {Link, useParams} from "react-router-dom";

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                <Link to={`/project/${project.id}/`}>{project.id}</Link>
            </td>
            <td>{project.name}</td>
            <td>{project.users}</td>
            <td>{project.repository}</td>
        </tr>
    )
}

const ProjectList = ({projects}) => {
    return (
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>NAME</th>
                    <th>USERS</th>
                    <th>URL REPO</th>
                </tr>
            </thead>
            <tbody>
                {projects.map((project) => <ProjectItem key={project.id} item={project} />)}
            </tbody>
        </table>
    )
}

const ProjectUserItem = ({item}) => {
    return (
        <li>
            {item.username} ({item.email}
        </li>
    )
}

const ProjectDetail = ({getProject, item}) => {
    let {id} = useParams();
    if (!Object.keys(item).length || item.id !== +id) {
        getProject(id);
    }
    let users = item.users ? item.users : [];
    return (
        <div>
            <h1>{item.name}</h1>
            Repo URL: <a href={item.repository}>{item.repository}</a>
            Users:
            <ol>
                {users.map((user) => <ProjectUserItem key={user.id} item={user}/>)}
            </ol>
        </div>
    )
}
export {ProjectDetail, ProjectList};
