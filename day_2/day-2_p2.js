import fs from 'fs';

function sum_of_power_sets(fileContent) {
    const lines = fileContent.trim().split('\n');
    let sum_of_powers = 0;

    lines.forEach(line => {
        const game = line.split(': ')[1].split('; ');

        let min_cubes = {
            'red' : 0,
            'green' : 0,
            'blue': 0
        }

        for (let config = 0; config < game.length; config++) {
            let cubes = game[config].split(', ');

            for (let cube of cubes) {
                let [count, color] = cube.split(' ');
                count = parseInt(count);

                min_cubes[color] = Math.max(min_cubes[color], count)
            }
        }
        
        let multipliedValues = 1;

        for (let cube_color in min_cubes) {
            multipliedValues *= min_cubes[cube_color]
        }

        sum_of_powers += multipliedValues

    });

    return sum_of_powers;
}

const fileContent = fs.readFileSync("./day_2.in", 'utf-8');
const sum_of_powers = sum_of_power_sets(fileContent);

console.log(sum_of_powers);
