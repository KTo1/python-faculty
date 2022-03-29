"use strict";
const settings = {
  rowsCount: 21,
  colsCount: 21,
  speed: 2,
  winFoodCount: 50,
};

const config = {
  settings,

  init(userSettings) {
    Object.assign(this.settings, userSettings);
  },

  getRowsCount() {
    return this.settings.rowsCount;
  },

  getColsCount() {
    return this.settings.colsCount;
  },

  getSpeed() {
    return this.settings.speed;
  },

  setSpeed(speed) {
    this.settings.speed = speed;
  },  

  getWinFoodCount() {
    return this.settings.winFoodCount;
  },

  validate() {
    const result = {
      isValid: true,
      errors: [],
    };

    if (this.getRowsCount() < 10 || this.getRowsCount() > 30) {
      result.isValid = false;
      result.errors.push('Неверные настройки, значение rowsCount должно быть в диапазоне [10, 30].');
    }

    if (this.getColsCount() < 10 || this.getColsCount() > 30) {
      result.isValid = false;
      result.errors.push('Неверные настройки, значение colsCount должно быть в диапазоне [10, 30].');
    }

    if (this.getSpeed() < 1 || this.getSpeed() > 10) {
      result.isValid = false;
      result.errors.push('Неверные настройки, значение speed должно быть в диапазоне [1, 10].');
    }

    if (this.getWinFoodCount() < 5 || this.getWinFoodCount() > 50) {
      result.isValid = false;
      result.errors.push('Неверные настройки, значение winFoodCount должно быть в диапазоне [5, 50].');
    }

    return result;
  }
};

const map = {
  cells: {}, // {x1_y1: td, x2_y1: td, ...};
  usedCells: [],

  init(rowsCount, colsCount) {
    const table = document.getElementById('game');
    table.innerHTML = '';

    this.cells = {};
    this.usedCells = [];

    for (let row = 0; row < rowsCount; row++) {
      const tr = document.createElement('tr');
      tr.classList.add('row');
      table.appendChild(tr);

      for (let col = 0; col < colsCount; col++) {
        const td = document.createElement('td');
        td.classList.add('cell');
        tr.appendChild(td);

        const tdKey = `x${ col }_y${ row }`;
        this.cells[tdKey] = td;
      }
    }
  },

  render(snakePointsArray, foodPoint, wallPoint) {

    for (const cell of this.usedCells) {
      cell.className = 'cell';
    }

    this.usedCells = [];

    snakePointsArray.forEach((snakePoint, index) => {
      const snakePointKey = `x${ snakePoint.x }_y${ snakePoint.y }`;
      const snakeCell = this.cells[snakePointKey];
      snakeCell.classList.add(index === 0 ? 'snakeHead' : 'snakeBody');
      this.usedCells.push(snakeCell);
    });

    const foodPointKey = `x${ foodPoint.x }_y${ foodPoint.y }`;
    const foodCell = this.cells[foodPointKey];

    foodCell.classList.add('food');

    const wallPointKey = `x${ wallPoint.x }_y${ wallPoint.y }`;
    const wallCell = this.cells[wallPointKey];

    wallCell.classList.add('wall');

    
    this.usedCells.push(foodCell);
    this.usedCells.push(wallCell);
  },
};

const snake = {
  body: [],
  direction: null,
  lastStepDirection: null,
  max_col: 0,
  max_row: 0,

  init(startBodyArray, direction, max_col, max_row) {
    this.body = startBodyArray;
    this.direction = direction;
    this.lastStepDirection = direction;
    this.max_col = max_col;
    this.max_row = max_row;
  },

  getLength(){
    return this.body.length;
  },

  getBody() {
    return this.body;
  },

  getLastStepDirection() {
    return this.lastStepDirection;
  },

  setDirection(direction) {
    this.direction = direction;
  },

  isOnPoint(point) {
    return this.getBody().some((snakePoint) => snakePoint.x === point.x && snakePoint.y === point.y);
  },

  makeStep() {
    const snakeBody = this.getBody();
    this.lastStepDirection = this.direction;
    snakeBody.unshift(this.getNextStepHeadPoint());
    snakeBody.pop();
  },

  growUp() {
    const snakeBody = this.getBody();
    const lastSnakeBodyPointIndex = snakeBody.length - 1;
    const lastSnakeBodyPoint = snakeBody[lastSnakeBodyPointIndex];
    const lastSnakeBodyPointClone = Object.assign({}, lastSnakeBodyPoint);

    snakeBody.push(lastSnakeBodyPointClone);
  },

  getNextStepHeadPoint() {
    const headPoint = this.getBody()[0];

    const max_col = this.max_col;
    const max_row = this.max_row;

    switch (this.direction) {
      case 'up'   : return { x: headPoint.x , y: (headPoint.y - 1) < 0 ? (max_row - 2) - (headPoint.y - 1) % max_row: (headPoint.y - 1) % max_row };
      case 'down' : return { x: headPoint.x , y: (headPoint.y + 1) % max_row };
      case 'right': return { x: (headPoint.x + 1) % max_col , y: headPoint.y };      
      case 'left' : return { x: (headPoint.x - 1) < 0 ? (max_col - 2) - (headPoint.x - 1) % max_col : (headPoint.x - 1) % max_col , y: headPoint.y };
    }
  }
};

const food = {
  x: null,
  y: null,

  getCoordinates() {
    return {
      x: this.x,
      y: this.y,
    }
  },

  setCoordinates(point) {
    this.x = point.x;
    this.y = point.y;
  },

  isOnPoint(point) {
    return this.x === point.x && this.y === point.y;
  }
};

const wall = {
  x: null,
  y: null,

  getCoordinates() {
    return {
      x: this.x,
      y: this.y,
    }
  },

  setCoordinates(point) {
    this.x = point.x;
    this.y = point.y;
  },

  isOnPoint(point) {
    return this.x === point.x && this.y === point.y;
  }
};

const hud = {
  render(data){

    const table_hud = document.getElementById('game-hud');
    table_hud.innerHTML = '';

    table_hud.innerHTML = `
          
      <table class="tg">
      <colgroup>
        <col style="">
        <col style="">
        <col style="width: 72px">
        <col style="">
        <col style="">
      </colgroup>

      <thead>
      <tr>
      <th class="tg-0lax">Легенда:</th>
      <th class="tg-0lax"></th>
      <th class="tg-0lax"></th>
      <th class="tg-0lax">Правила:</th>
      <th class="tg-0lax"></th>
      </tr>
      </thead>
      <tbody>
      <tr>
      <td class="tg-0lax"></td>
      <td class="cell snakeHead"></td>
      <td class="tg-0lax">- голова</td>
      <td class="tg-0lax"></td>
      <td class="tg-0lax" rowspan="4">Используйте весь свой интеллект, всю свою хитрость и ловкость, 
        а так же стрелки курсора для перемещения по полю и охоты на кролика. Не врезайтесь в стену и не ешьте свой хвост.
      </td>
      </tr>
      <tr>
      <td class="tg-0lax"></td>
      <td class="cell snakeBody"></td>
      <td class="tg-0lax">- хвост</td>
      <td class="tg-0lax"></td>
      </tr>
      <tr>
      <td class="tg-0lax"></td>
      <td class="cell food"></td>
      <td class="tg-0lax">- еда</td>
      <td class="tg-0lax"></td>
      </tr>
      <tr>
      <td class="tg-0lax"></td>
      <td class="cell wall"></td>
      <td class="tg-0lax">- стена</td>
      <td class="tg-0lax"></td>
      </tr>
      </tbody>
      </table>`;

    const tr_score = document.createElement('tr');
    tr_score.classList.add('row-hud');
    table_hud.appendChild(tr_score);

    const td_score = document.createElement('td');
    td_score.classList.add('cell-hud');
    td_score.textContent = `Счет: ${data.score} кроликов из ${data.total} необходимых `;
    tr_score.appendChild(td_score);

  },
};

const status = {
  condition: null,

  setPlaying() {
    this.condition = 'playing';
  },

  setStopped() {
    this.condition = 'stopped';
  },

  setFinished() {
    this.condition = 'finished';
  },

  isPlaying() {
    return this.condition === 'playing';
  },

  isStopped() {
    return this.condition === 'stopped';
  },
};

const game = {
  config,
  map,
  snake,
  food,
  hud,
  wall, 
  status,
  tickInterval: null,

  init(userSettings = {}) {
    this.config.init(userSettings);
    const validationData = this.config.validate();

    if (!validationData.isValid) {
      for (const err of validationData.errors) {
        console.log(err);
      }

      return;
    }

    this.map.init(this.config.getRowsCount(), this.config.getColsCount());

    this.setEventHandlers();
    this.reset();
  },

  reset() {
    this.stop();
    this.snake.init(this.getStartSnakeBody(), 'up', this.config.getColsCount(), this.config.getRowsCount());
    this.food.setCoordinates(this.getRandomFreeCoordinate());
    this.wall.setCoordinates(this.getRandomFreeCoordinate());    
    this.render();
  },

  getStartSnakeBody() {
    return [
      {
        x: Math.floor(this.config.getColsCount() / 2),
        y: Math.floor(this.config.getRowsCount() / 2),
      },
    ];
  },

  getRandomFreeCoordinate() {
    const exclude = [this.food.getCoordinates(), ...this.snake.getBody(), this.wall.getCoordinates()] ;

    while (true) {
      const randomPoint = {
        x: Math.floor(Math.random() * this.config.getColsCount()),
        y: Math.floor(Math.random() * this.config.getRowsCount()),
      };

      if (!exclude.some((exPoint) => randomPoint.x === exPoint.x && randomPoint.y === exPoint.y)) {
        return randomPoint;
      }
    }
  },

  setEventHandlers() {
    document.getElementById('playButton').addEventListener('click', () => {
      this.playClickHandler();
    });
    document.getElementById('newGameButton').addEventListener('click', () => {
      this.newGameClickHandler();
    });
    document.addEventListener('keydown', (event) => this.keyDownHandler(event));
  },

  playClickHandler() {
    if (this.status.isPlaying()) {
      this.stop();
    } else if (this.status.isStopped()) {
      this.play();
    }
  },

  newGameClickHandler() {
    this.reset();
  },

  keyDownHandler(event) {
    if (!this.status.isPlaying()) return;

    const direction = this.getDirectionByCode(event.code);
    if (this.canSetDirection(direction)) this.snake.setDirection(direction);
  },

  getDirectionByCode(code) {
    switch (code) {
      case 'KeyW':
      case 'ArrowUp':
        return 'up';
      case 'KeyD':
      case 'ArrowRight':
        return 'right';
      case 'KeyS':
      case 'ArrowDown':
        return 'down';
      case 'KeyA':
      case 'ArrowLeft':
        return 'left';
    }
  },

  canSetDirection(direction) {
    const lastStepDirection = this.snake.getLastStepDirection();

    return direction === 'up' && lastStepDirection !== 'down' ||
        direction === 'right' && lastStepDirection !== 'left' ||
        direction === 'down' && lastStepDirection !== 'up' ||
        direction === 'left' && lastStepDirection !== 'right';
  },

  stop() {
    this.status.setStopped();
    clearInterval(this.tickInterval);
    this.setPlayButtonState('Старт');
  },

  finish() {
    this.status.setFinished();
    clearInterval(this.tickInterval);
    this.setPlayButtonState('Игра окончена', true);
  },

  play() {
    this.status.setPlaying();
    this.tickInterval = setInterval(() => this.tickHandler(), 1000 / this.config.getSpeed());
    this.setPlayButtonState('Стоп');
  },

  setPlayButtonState(text, isDisabled = false) {
    const playButton = document.getElementById('playButton');

    playButton.textContent = text;

    isDisabled
        ? playButton.classList.add('disabled')
        : playButton.classList.remove('disabled');
  },

  tickHandler() {
    if (!this.canMakeStep()) return this.finish();

    if (this.food.isOnPoint(this.snake.getNextStepHeadPoint())) {
      this.snake.growUp();
      this.food.setCoordinates(this.getRandomFreeCoordinate());
      this.wall.setCoordinates(this.getRandomFreeCoordinate());

      if (this.isGameWon()) this.finish();
    }

    if (this.wall.isOnPoint(this.snake.getNextStepHeadPoint())) {
      this.finish();
    };

    this.snake.makeStep();
    this.render();
  },

  canMakeStep() {
    const nextStepSnakeHeadPoint = this.snake.getNextStepHeadPoint();

    return !this.snake.isOnPoint(nextStepSnakeHeadPoint);
        // && nextStepSnakeHeadPoint.x < this.config.getColsCount()
        // && nextStepSnakeHeadPoint.y < this.config.getRowsCount()
        // && nextStepSnakeHeadPoint.x >= 0
        // && nextStepSnakeHeadPoint.y >= 0;
  },

  isGameWon() {
    return this.snake.getLength() > this.config.getWinFoodCount();
  },

  render() {
    this.map.render(this.snake.getBody(), this.food.getCoordinates(), this.wall.getCoordinates());
    this.hud.render({score: this.snake.getLength() - 1, total: this.config.getWinFoodCount()});
  }
};

game.init({ speed: 5 });
