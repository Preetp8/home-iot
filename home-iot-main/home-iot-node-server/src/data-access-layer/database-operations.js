import pg from 'pg';
import { getWeatherByHour } from '../outbound-requests/meteostat-api.js';

const { Client } = pg;
const client = new Client({
    user: 'Team1',
    host: '138.26.48.83',
    database: 'Team1DB',
    password: 'team1',
    port: 5432
});
client.connect();

export async function createHvacTable() {
    const tableStatement = `
    CREATE TABLE IF NOT EXISTS hvac (
        user_name varchar(50) NOT NULL,
        set_temp integer NOT NULL DEFAULT '72',
        inner_temp integer NOT NULL DEFAULT '72',
        outer_temp integer NOT NULL DEFAULT '60',
        PRIMARY KEY (user_name)
    )
    `;

    let tableCreationResult;
    let adminCreated = false;
    try {
        tableCreationResult = await client.query(tableStatement);

        const selectStatement = 'SELECT * FROM hvac WHERE user_name = \'admin\'';
        const selectResult = await client.query(selectStatement);
        if(selectResult.rows.length > 0)
            adminCreated = true;
    } catch(err) {
        console.log('Error creating hvac table...');
        console.error(err);
    }

    const currentDate = new Date();
    const currentHour = currentDate.getHours();
    const payload = await getWeatherByHour(currentDate);
    if(!adminCreated) {
        try {
            console.log(tableCreationResult);
    
            const currentOutsideTemperature = payload ? payload.data[currentHour].temp : null;
            const insert = currentOutsideTemperature ? 'INSERT INTO hvac(user_name, outer_temp) VALUES ($1, $2)' : 'INSERT INTO hvac(user_name) VALUES ($1)';
            const values = currentOutsideTemperature ? ['admin', currentOutsideTemperature] : ['admin'];
            const insertResult = await client.query(insert, values);
    
            console.log('Logging Insert Statement...');
            console.log(insertResult);
        }
        catch(err) {
            console.log('Error inserting admin into hvac table...');
            console.error(err);
        }
    } else {
        try {
            const meteostatTemperature = payload ? payload.data[currentHour].temp : null;
            if(meteostatTemperature) {
                const update = `UPDATE hvac SET outer_temp = ${Math.floor(meteostatTemperature)} WHERE user_name = 'admin'`;
                const result = await client.query(update);

                console.log('Logging Update Statement...');
                console.log(result);
            }
        } catch(err) {
            console.log('Error updating admin row in hvac table...');
            console.error(err);
        }
    }
}

export async function getAdminHvac() {
    const query = 'SELECT * FROM hvac WHERE user_name = \'admin\'';
    
    try {
        const queryResult = await client.query(query);
        console.log('hvac query result...');
        console.log(queryResult);

        return queryResult.rows[0];
    } catch (err) {
        console.log('Error querying hvac table...');
        console.error(err);
    }
}

export async function updateAdminHvac(hvac) {
    const sqlStatement = `
    UPDATE hvac
    SET set_temp = $2,
    inner_temp = $3,
    outer_temp = $4
    WHERE user_name = $1
    `;
    const values = ['admin', hvac.currentSetTemp, hvac.innerTemp, hvac.outerTemp];

    await client.query(sqlStatement, values);
}

export async function createWeatherTable() {
    const tableStatement = `
    CREATE TABLE IF NOT EXISTS weather (
        temperature integer NOT NULL DEFAULT '70',
        air_quality integer NOT NULL DEFAULT '67',
        wind_speed integer DEFAULT '3',
        precipitation integer DEFAULT '10'
    )
    `;

    let tableCreationResult;
    let adminCreated = false;
    try {
        tableCreationResult = await client.query(tableStatement);

        const selectStatement = 'SELECT * FROM weather';
        const selectResult = await client.query(selectStatement);
        if(selectResult.rows.length > 0)
            adminCreated = true;
    } catch(err) {
        console.log('Error creating weather table...');
        console.error(err);
    }

    if(!adminCreated) {
        try {
            console.log(tableCreationResult);
    
            const currentDate = new Date();
            const payload = await getWeatherByHour(currentDate);
            const currentHour = currentDate.getHours();
            const currentOutsideTemperature = payload ? payload.data[currentHour].temp : null;
            
            const insert = currentOutsideTemperature ? 'INSERT INTO weather(temperature) VALUES ($1)' : 'INSERT INTO weather(temperature) VALUES ($1)';
            const values = currentOutsideTemperature ? ['admin', currentOutsideTemperature] : ['admin'];
            const insertResult = await client.query(insert, values);
    
            console.log('Logging Insert Statement...');
            console.log(insertResult);
        }
        catch(err) {
            console.log('Error inserting admin into weather table...');
            console.error(err);
        }
    }
}

export async function getAdminWeather() {
    const query = 'SELECT * FROM weather';
    
    try {
        const queryResult = await client.query(query);
        console.log('weather query result...');
        console.log(queryResult);

        return queryResult.rows[0];
    } catch (err) {
        console.log('Error querying weather table...');
        console.error(err);
    }
}

export async function updateAdminWeather(weather) {
    const sqlStatement = `
    UPDATE weather
    temperature = $3,
    air_quality = $4,
    wind_speed = $5,
    precipitation = $6
    `;
    const values = ['admin', weather.temperature, weather.air_quality, weather.wind_speed, weather.precipitation];

    await client.query(sqlStatement, values);
}

export async function createUsageTable() {
    const tableStatement = `
    CREATE TABLE IF NOT EXISTS usage (
        water float DEFAULT '100.0',
        cost_of_water float DEFAULT '50.0',
        electricity float DEFAULT '100.0',
        cost_of_electricity float DEFAULT '50.0',
        date date,
        gas float DEFAULT '10.0',
        cost_of_gas float DEFAULT '10.0'
    )
    `;

    let tableCreationResult;
    let adminCreated = false;
    try {
        tableCreationResult = await client.query(tableStatement);

        const selectStatement = 'SELECT * FROM usage';
        const selectResult = await client.query(selectStatement);
        if(selectResult.rows.length > 0)
            adminCreated = true;
    } catch(err) {
        console.log('Error creating usage table...');
        console.error(err);
    }

    if(!adminCreated) {
        try {
            console.log(tableCreationResult);
    
            const currentDate = new Date();
            const payload = await getWeatherByHour(currentDate);
            const currentHour = currentDate.getHours();
            const currentOutsideTemperature = payload ? payload.data[currentHour].temp : null;
            
            const insert = currentOutsideTemperature ? 'INSERT INTO usage(gas, electricity) VALUES ($1, $2)' : 'INSERT INTO usage(gas, electricity) VALUES ($1)';
            const values = currentOutsideTemperature ? ['admin', currentOutsideTemperature] : ['admin'];
            const insertResult = await client.query(insert, values);
    
            console.log('Logging Insert Statement...');
            console.log(insertResult);
        }
        catch(err) {
            console.log('Error inserting admin into usage table...');
            console.error(err);
        }
    }
}

export async function getAdminUsage() {
    const query = 'SELECT * FROM usage';
    
    try {
        const queryResult = await client.query(query);
        console.log('usage query result...');
        console.log(queryResult);

        return queryResult.rows[0];
    } catch (err) {
        console.log('Error querying usage table...');
        console.error(err);
    }
}

export async function updateAdminUsage(weather) {
    const sqlStatement = `
    UPDATE weather

    water = $3,
    cost_of_water = $4,
    electricity = $5,
    cost_of_electricity = $6
    gas = $7,
    cost_of_gas = $8
    `;
    const values = ['admin', weather.water, weather.cost_of_water, weather.electricity, weather.cost_of_electricity, weather.gas, weather.cost_of_gas];

    await client.query(sqlStatement, values);
}


export function closeDbConnection() {
    client.end((err) => {
        console.log('backend has disconnected from db')
        if (err) {
            console.log('error during disconnection', err.stack)
        }
    });
}