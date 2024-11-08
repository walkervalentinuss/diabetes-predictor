document.getElementById('diabetes-form').addEventListener('input', function(event) {
    const target = event.target;
    const fieldsToValidate = ['glucose', 'bloodPressure', 'skinThickness', 'insulin', 'bmi', 'age'];

    if (fieldsToValidate.includes(target.id)) {
        const value = parseFloat(target.value);
        if (value === 0) {
            target.classList.add('is-invalid');
            target.nextElementSibling.style.display = 'block';
        } else {
            target.classList.remove('is-invalid');
            target.nextElementSibling.style.display = 'none';
        }
    }
});

document.getElementById('diabetes-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const invalidFields = document.querySelectorAll('.is-invalid');
    if (invalidFields.length > 0) return;

    const data = {
        input: [
            parseFloat(document.getElementById('pregnancies').value),
            parseFloat(document.getElementById('glucose').value),
            parseFloat(document.getElementById('bloodPressure').value),
            parseFloat(document.getElementById('skinThickness').value),
            parseFloat(document.getElementById('insulin').value),
            parseFloat(document.getElementById('bmi').value),
            parseFloat(document.getElementById('diabetesPedigreeFunction').value),
            parseFloat(document.getElementById('age').value)
        ]
    };

    try {
        const response = await fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        const prediction = result.prediction === 1 ? "Diabetes Detected" : "No Diabetes Detected";

        document.getElementById('result').innerHTML = `
            <div class="alert alert-info">${prediction}</div>
        `;

        document.getElementById('diabetes-form').reset();
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('result').innerHTML = `
            <div class="alert alert-danger">Error making prediction. Please try again.</div>
        `;
    }
});