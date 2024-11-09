async function fetchOptionPrices() {
    const response = await fetch('/option-prices');
    const data = await response.json();
    document.getElementById('optionPrices').innerText = 
        `Call Price: $${data.callPrice}, Put Price: $${data.putPrice}`;
}

setInterval(fetchOptionPrices, 5000); // Update every 5 seconds
