

function add_books(){
    const tables=document.getElementById('book_table');
    let table_chiled=document.createElement('div');
    table_chiled.innerHTML('<td>1</td><td>羊の冒険</td><td>〇</td><td>None</td>')
    tables.appendChild(table_chiled);
    console.log('push')
}