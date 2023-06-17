const globalClock = document.querySelector('.global-clock');
const clockUrl = 'http://localhost:8000/clock';
const eventSource = new EventSource(clockUrl);

eventSource.onmessage = event => {
    const currentTime = event.data;
    const globalClockText = globalClock.children[0];
    globalClockText.textContent = JSON.parse(currentTime);

    console.log(event);
}

// This stops the frontend from attempting to make a connection to receive server sent events when an error occurs.
// This Prevents clogging the console with the errors that occur repeatedly when the server is down.
eventSource.onerror = event => {
    console.log(event);
    eventSource.close();
}