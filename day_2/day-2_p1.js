import fs from 'fs';

const actual = {
    'red': 12,
    'green': 13,
    'blue': 14
};

function sum_of_possible_IDs(fileContent) {
    const lines = fileContent.trim().split('\n');
    let sum_game_numbers = 0;

    lines.forEach(line => {
        const game = line.split(': ')[1].split('; ');
        const game_number = parseInt(line.split(': ')[0].split(" ")[1]);

        let isPossible = true;

        for (let config = 0; config < game.length && isPossible; config++) {
            let cubes = game[config].split(', ');

            for (let cube of cubes) {
                let [count, color] = cube.split(' ');
                count = parseInt(count);

                if (count > actual[color]) {
                    isPossible = false;
                    break;
                }
            }
        }

        if (isPossible) {
            sum_game_numbers += game_number;
        }
    });

    return sum_game_numbers;
}

const fileContent = fs.readFileSync("./day_2.in", 'utf-8');
const sum_game_numbers = sum_of_possible_IDs(fileContent);

console.log(sum_game_numbers);
