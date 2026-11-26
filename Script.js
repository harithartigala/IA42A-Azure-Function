const nameInput = document.getElementById('nameInput');
const drawBtn = document.getElementById('drawBtn');
const result = document.getElementById('result');

drawBtn.addEventListener('click', async () => {
    const name = nameInput.value.trim();
    if (!name) {
        result.textContent = '名前を入力してください';
        return;
    }

    result.textContent = '占い中...';

    try {
        // APIを呼び出す（名前はURLで使える形に変換して送る）
        const response = await fetch(`/api/fortune?name=${encodeURIComponent(name)}`);
        const data = await response.json();

        if (response.ok) {
            result.textContent = `${data.name}さんの運勢は「${data.result}」です！`;
        } else {
            result.textContent = `エラー: ${data.error}`;
        }
    } catch (error) {
        result.textContent = `エラー: ${error.message}`;
    }
});