import React from "react";
import {useParams} from "react-router-dom";

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td>{project.name}</td>
            <td>{project.users}</td>
            <td>{project.repository}</td>
        </tr>
    )
}

const ProjectItemList = ({projects}) => {
    let {id} = useParams();
    let filteredProjects = projects.filter((project) => project.id === +id);
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
            {filteredProjects.map((project) => <ProjectItem key={project.id} project={project}/>)}
            </tbody>
        </table>
    )
}

export default ProjectItemList;
