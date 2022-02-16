/*
Создать функцию, генерирующую шахматную доску. При этом можно использовать любые html-теги по своему желанию. 
Доска должна быть разлинована соответствующим образом, т.е. чередовать черные и белые ячейки. 
Строки должны нумероваться числами от 1 до 8, столбцы – латинскими буквами A, B, C, D, E, F, G, H. 
(использовать createElement / appendChild)
*/

console.log('Task - 1');
console.log('---------------------------------------------');

function draw_board(container, rowCount=8, colCount=8){

    colorBlack = '#000';
    colorWhite = '#FFF';

    table_board = document.createElement('table');
    table_board.id = "table_board";
    container.appendChild(table_board);

    for (let row = 0; row < rowCount + 1; row++) {
        const tr = document.createElement('tr');
        table_board.appendChild(tr);
        for (let col = 0; col < colCount + 1; col++) {
            const td = document.createElement('td');
            if (row == 0 || col == 0) {
                td.style.border = '0em';
                td.style.backgroundColor = colorWhite;
                td.innerText = (col == 0 && row != 0) ? row : String.fromCharCode(64 + col);            
            } else {
                td.style.backgroundColor = (col + row) % 2 == 0 ? colorWhite : colorBlack;
            };        
            tr.appendChild(td);
        };
    };
};

draw_board(document.getElementById('board'))

console.log('---------------------------------------------');
