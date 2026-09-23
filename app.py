from flask import Flask

app = Flask(**name**)

@app.route("/")
def home():
return """

<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PaaSify | Flask Application</title>

```
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: Arial, sans-serif;
    }

    html {
        scroll-behavior: smooth;
    }

    body {
        background: #f7f8fc;
        color: #1f2937;
    }

    nav {
        width: 100%;
        padding: 20px 8%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: white;
        position: sticky;
        top: 0;
        z-index: 100;
        box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    }

    .logo {
        font-size: 24px;
        font-weight: bold;
        color: #2563eb;
    }

    nav ul {
        list-style: none;
        display: flex;
        gap: 30px;
    }

    nav a {
        text-decoration: none;
        color: #374151;
        font-weight: 500;
    }

    nav a:hover {
        color: #2563eb;
    }

    .hero {
        min-height: 82vh;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 70px 8%;
        gap: 50px;
        background: linear-gradient(135deg, #eef4ff, #ffffff);
    }

    .hero-text {
        max-width: 600px;
    }

    .tag {
        display: inline-block;
        background: #dbeafe;
        color: #2563eb;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 14px;
        font-weight: bold;
        margin-bottom: 20px;
    }

    .hero h1 {
        font-size: 52px;
        line-height: 1.15;
        margin-bottom: 20px;
        color: #111827;
    }

    .hero h1 span {
        color: #2563eb;
    }

    .hero p {
        font-size: 18px;
        line-height: 1.7;
        color: #6b7280;
        margin-bottom: 30px;
    }

    .button {
        display: inline-block;
        padding: 14px 25px;
        background: #2563eb;
        color: white;
        text-decoration: none;
        border-radius: 8px;
        font-weight: bold;
        margin-right: 10px;
    }

    .button:hover {
        background: #1d4ed8;
    }

    .button-outline {
        background: white;
        color: #2563eb;
        border: 1px solid #2563eb;
    }

    .button-outline:hover {
        background: #eff6ff;
    }

    .hero-card {
        width: 390px;
        padding: 35px;
        background: white;
        border-radius: 20px;
        box-shadow: 0 15px 40px rgba(37,99,235,0.12);
    }

    .server {
        padding: 18px;
        margin: 15px 0;
        border-radius: 10px;
        background: #f3f4f6;
        border-left: 5px solid #2563eb;
    }

    .server strong {
        display: block;
        margin-bottom: 5px;
    }

    .status {
        color: #16a34a;
        font-size: 14px;
    }

    section {
        padding: 80px 8%;
    }

    .section-title {
        text-align: center;
        margin-bottom: 50px;
    }

    .section-title h2 {
        font-size: 36px;
        color: #111827;
        margin-bottom: 12px;
    }

    .section-title p {
        color: #6b7280;
    }

    .cards {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 25px;
    }

    .card {
        background: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.06);
        transition: 0.3s;
    }

    .card:hover {
        transform: translateY(-6px);
    }

    .icon {
        font-size: 32px;
        margin-bottom: 18px;
    }

    .card h3 {
        margin-bottom: 12px;
        color: #111827;
    }

    .card p {
        color: #6b7280;
        line-height: 1.6;
    }

    .steps {
        max-width: 900px;
        margin: auto;
    }

    .step {
        display: flex;
        gap: 20px;
        background: white;
        padding: 25px;
        margin-bottom: 18px;
        border-radius: 12px;
        box-shadow: 0 5px 20px rgba(0,0,0,0.05);
    }

    .number {
        min-width: 45px;
        height: 45px;
        background: #2563eb;
        color: white;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
    }

    .step h3 {
        margin-bottom: 7px;
    }

    .step p {
        color: #6b7280;
    }

    footer {
        background: #111827;
        color: white;
        text-align: center;
        padding: 30px;
    }

    footer p {
        color: #9ca3af;
        margin-top: 8px;
    }

    @media (max-width: 850px) {
        .hero {
            flex-direction: column;
            text-align: center;
        }

        .hero h1 {
            font-size: 40px;
        }

        .hero-card {
            width: 100%;
            max-width: 390px;
        }

        .cards {
            grid-template-columns: 1fr;
        }
    }

    @media (max-width: 500px) {
        nav ul {
            display: none;
        }

        section {
            padding: 60px 5%;
        }
    }
</style>
```

</head>

<body>

```
<nav>
    <div class="logo">PaaSify</div>

    <ul>
        <li><a href="#home">Home</a></li>
        <li><a href="#features">Features</a></li>
        <li><a href="#workflow">How It Works</a></li>
    </ul>
</nav>

<section class="hero" id="home">

    <div class="hero-text">

        <div class="tag">☁ Platform as a Service</div>

        <h1>
            Build. Deploy.
            <span>Scale.</span>
        </h1>

        <p>
            A simple Flask web application demonstrating how
            Platform as a Service makes it easy to deploy and
            host web applications on the cloud.
        </p>

        <a href="#features" class="button">Explore Application</a>
        <a href="#workflow" class="button button-outline">Learn More</a>

    </div>

    <div class="hero-card">

        <h2>Application Status</h2>

        <div class="server">
            <strong>Flask Application</strong>
            <span class="status">● Running</span>
        </div>

        <div class="server">
            <strong>Cloud Deployment</strong>
            <span class="status">● Active</span>
        </div>

        <div class="server">
            <strong>PaaS Platform</strong>
            <span class="status">● Connected</span>
        </div>

    </div>

</section>

<section id="features">

    <div class="section-title">
        <h2>Key Features</h2>
        <p>Understanding the benefits of Platform as a Service</p>
    </div>

    <div class="cards">

        <div class="card">
            <div class="icon">☁️</div>
            <h3>Cloud Deployment</h3>
            <p>
                Deploy applications to the cloud without
                managing physical servers or infrastructure.
            </p>
        </div>

        <div class="card">
            <div class="icon">⚡</div>
            <h3>Easy Deployment</h3>
            <p>
                Connect your source code and deploy your
                application with a simple configuration.
            </p>
        </div>

        <div class="card">
            <div class="icon">📈</div>
            <h3>Scalable Platform</h3>
            <p>
                PaaS provides an environment where applications
                can be managed and scaled efficiently.
            </p>
        </div>

    </div>

</section>

<section id="workflow">

    <div class="section-title">
        <h2>How This Project Works</h2>
        <p>The complete deployment workflow</p>
    </div>

    <div class="steps">

        <div class="step">
            <div class="number">1</div>
            <div>
                <h3>Develop</h3>
                <p>Create the Flask application using Python.</p>
            </div>
        </div>

        <div class="step">
            <div class="number">2</div>
            <div>
                <h3>Test</h3>
                <p>Run and test the application using Google Colab.</p>
            </div>
        </div>

        <div class="step">
            <div class="number">3</div>
            <div>
                <h3>Store</h3>
                <p>Upload the application files to GitHub.</p>
            </div>
        </div>

        <div class="step">
            <div class="number">4</div>
            <div>
                <h3>Deploy</h3>
                <p>Deploy the Flask application using Render.</p>
            </div>
        </div>

    </div>

</section>

<footer>
    <h3>PaaSify</h3>
    <p>Flask PaaS Deployment Experiment • Built for learning</p>
</footer>
```

</body>
</html>
    """

if **name** == "**main**":
app.run(host="0.0.0.0", port=5000)
