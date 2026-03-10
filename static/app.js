document.getElementById('getLinkBtn').addEventListener('click', async function() {
    const urlInput = document.getElementById('videoUrl').value.trim();
    const resultDiv = document.getElementById('result');
    const getLinkBtn = document.getElementById('getLinkBtn');

    if (!urlInput) {
        resultDiv.innerHTML = '<div class="alert alert-warning">Please enter a valid URL.</div>';
        return;
    }

    resultDiv.innerHTML = '<div class="alert alert-info">Extracting link... Please wait. This may take a moment.</div>';
    getLinkBtn.disabled = true;

    try {
        const response = await fetch('/api/get-link', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url: urlInput })
        });

        const data = await response.json();

        if (data.success) {
            resultDiv.innerHTML = `
                <div class="alert alert-success">
                    <strong>Ready:</strong> ${data.title}<br><br>
                    <a href="${data.video_url}" target="_blank" class="btn btn-success w-100 fw-bold">👉 Click Here to Download</a>
                    <small class="d-block mt-2 text-muted text-center">Note: Right-click the button and select 'Save link as...' if it opens in the browser.</small>
                </div>
            `;
        } else {
            resultDiv.innerHTML = `<div class="alert alert-danger">Error: ${data.error}</div>`;
        }
    } catch (error) {
        resultDiv.innerHTML = `<div class="alert alert-danger">Network Error: Could not connect to the server.</div>`;
    } finally {
        getLinkBtn.disabled = false;
    }
});

document.getElementById('resetBtn').addEventListener('click', function() {
    document.getElementById('videoUrl').value = '';
    document.getElementById('result').innerHTML = '';
});