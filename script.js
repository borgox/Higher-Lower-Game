document.addEventListener('DOMContentLoaded', function() {
    const guessForm = document.getElementById('guess-form');
    const guessInput = document.getElementById('guess-input');
    const guessButton = document.getElementById('guess-button');
    const resultDiv = document.getElementById('result');

    let winstreak = 0;
    let toGuess = genNumber();

    guessForm.addEventListener('submit', function(event) {
        event.preventDefault();
        submitGuess();
    });

    guessInput.addEventListener('keyup', function(event) {
        if (event.key === 'Enter') {
            event.preventDefault();
            submitGuess();
        }
    });

    function submitGuess() {
        const guess = parseInt(guessInput.value);

        if (!isNaN(guess)) {
            if (guess > toGuess) {
                resultDiv.textContent = 'Lower!';
            } else if (guess < toGuess) {
                resultDiv.textContent = 'Higher!';
            } else {
                winstreak++;
                resultDiv.innerHTML = '<h2>Congratulations!</h2><p>You guessed the number correctly!</p>';
                resultDiv.innerHTML += `<p>Win Streak: ${winstreak}</p>`;
                toGuess = genNumber();
            }
        }

        guessInput.value = '';
    }

    function genNumber() {
        return Math.floor(Math.random() * 10001);
    }
}); 