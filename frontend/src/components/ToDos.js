import React from "react";

const ToDoItem = ({todo}) => {
    return (
        <tr>
            <td>{todo.project}</td>
            <td>{todo.note_text}</td>
            <td>{todo.created_at}</td>
            <td>{todo.updated_at}</td>
            <td>{todo.author}</td>
        </tr>
    )
}

const ToDoList = ({todos}) => {
    return (
        <table>
            <thead>
                <tr><th>TODOS</th></tr>
                <tr>
                    <th>PROJECT</th>
                    <th>TEXT</th>
                    <th>CREATED AT</th>
                    <th>UPDATED AT</th>
                    <th>AUTHOR</th>
                </tr>
            </thead>
            <tbody>
                {todos.map((todo) => <ToDoItem key={todo.id} todo={todo} />)}
            </tbody>
        </table>
    )
}

export default ToDoList;
