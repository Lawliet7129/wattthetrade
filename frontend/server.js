const express = require('express');
const axios = require('axios');
const path = require('path');
const app = express();
const PORT = 3000;


app.use(express.static(path.join(__dirname, 'public')));

app.get('/option-prices', async (req, res) => {
    try {
        const response = await axios.get('http://localhost:5000/api/option-prices');
        res.json(response.data);
    } catch (error) {
        res.status(500).send('Error fetching option prices');
    }
});

app.listen(PORT, () => {
    console.log(`Frontend server running on http://localhost:${PORT}`);
});
