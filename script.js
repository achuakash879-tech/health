function checkDisease() {
    let symptoms = document.getElementById("symptoms").value;

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ symptoms: symptoms })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("disease").innerText = 
            "Possible Disease: " + data.disease;

        let doctorList = document.getElementById("doctors");
        doctorList.innerHTML = "";

        data.doctors.forEach(doc => {
            let li = document.createElement("li");
            li.innerText = doc;
            doctorList.appendChild(li);
        });
    });
}

function setReminder() {
    let medicine = document.getElementById("medicine").value;
    let time = document.getElementById("time").value;

    setTimeout(() => {
        alert("Time to take: " + medicine);
    }, time * 1000);

    alert("Reminder set!");
}