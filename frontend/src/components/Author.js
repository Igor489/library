import React from 'react';


const AuthorItem = ({author}) => {
    return (
        <tr>
            <td>{author.first_name}</td>
            <td>{author.last_name}</td>
            <td>{author.birthday_year}</td>
        </tr>
    )
}

const AuthorList = ({authors}) => {
    return (
        <table>
            <tr>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Birthday year</th>
            </tr>
            {authors.map((author) => <AuthorItem author={author} />)}
        </table>
    )
}

export default AuthorList
