// Function to determine the status color based on benchmarks
function getStatusColor(value, type, total) {
    console.log(type)
    if (type === "cpu_temp") {
        if (value < 50) return "green";
        if (value < 65) return "yellow";
        if (value < 75) return "orange";
        return "red";
    }
    if (type === "cpu_usage") {
        if (value < 50) return "green";
        if (value < 70) return "yellow";
        if (value < 90) return "orange";
        return "red";
    }
    if (type === "ram_usage") {
        if (value < (.60*Number(total))) return "green";
        if (value < (.75*Number(total))) return "yellow";
        if (value < (.90*Number(total))) return "orange";
        return "red";
    }
    if (type === "disk_usage") {
        if (value < (.70*Number(total))) return "green";
        if (value < (.80*Number(total))) return "yellow";
        if (value < (.95*Number(total))) return "orange";
        return "red";
    }
}

// Function to update stats dynamically
function updateStats(data) {
    const stats = {
        "cpu_temp": data.cpu_temp,
        "cpu_usage": data.cpu_usage,
        "ram_usage": data.ram_usage,
        "disk_usage": data.disk_usage,

        "ram_total": data.ram_total,
        "disk_total": data.disk_total
    };

    for (const key in stats) {
        const element = document.getElementById(key);
        if (element) {
            if(key == "cpu_temp") {
                element.innerText = `${stats[key]} °C`;
            }
            else if(key == "cpu_usage") {
                element.innerText = `${stats[key]}%`;
            } else if(key == "ram_usage") {
                element.innerText = `${stats[key]} MB / ${stats['ram_total']} MB`;
            } else if(key == "disk_usage") {
                element.innerText = `${stats[key]} GB / ${stats['disk_total']} GB`;
            } 

            if(key == "ram_usage") {
                element.style.color = getStatusColor(stats[key], key, data.ram_total);
            } else if(key == "disk_usage") {
                element.style.color = getStatusColor(stats[key], key, data.disk_total);
            } else {
                element.style.color = getStatusColor(stats[key], key);
            }
        }
    }
}














// Function to connect to SSE and update stats
function connectEventSource() {
    const eventSource = new EventSource("/stats");

    eventSource.onmessage = function(event) {
        const data = JSON.parse(event.data);
        updateStats(data);
    };

    eventSource.onerror = function() {
        console.error("Connection lost. Reconnecting...");
        eventSource.close();
        setTimeout(connectEventSource, 3000);
    };
}

document.addEventListener("DOMContentLoaded", connectEventSource);
