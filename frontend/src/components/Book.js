import React from 'react'


const BookItem = ({item}) => {
    return (
        <tr>
            <td>{item.id}</td>
            <td>{item.name}</td>
            <td>{item.author.name}</td>
        </tr>
    )
}


const BookList = ({items}) => {
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>NAME</th>
                <th>AUHTOR</th>
            </tr>
            {items.map((item) => <BookItem item={item} />)}
        </table>
    )
}


export default BookList
