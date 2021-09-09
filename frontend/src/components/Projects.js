import React from "react";
import {Link} from "react-router-dom";

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                <Link to={'/project/${project.id}/'}>{project.id}</Link>
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
                <tr><th>PROJECTS</th></tr>
                <tr>
                    <th>ID</th>
                    <th>NAME</th>
                    <th>USERS</th>
                    <th>URL REPO</th>
                </tr>
            </thead>
            <tbody>
                {projects.map((project) => <ProjectItem key={project.id} todo={project} />)}
            </tbody>
        </table>
    )
}
export default ProjectList;
