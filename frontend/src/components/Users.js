import React from "react";

const UserItem = ({user}) => {
    return (
        <tr>
            <td>{user.username}</td>
            <td>{user.first_name}</td>
            <td>{user.last_name}</td>
            <td>{user.email}</td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table className="table">
            <thead>
            <tr><th>USERS</th></tr>
                <tr>
                    <th>USER NAME</th>
                    <th>FIRST NAME</th>
                    <th>SECOND NAME</th>
                    <th>EMAIL</th>
                </tr>
            </thead>
            <tbody>
                {users.map((user) => <UserItem user={user}/>)}
            </tbody>
        </table>
    )
}
export default UserList;
