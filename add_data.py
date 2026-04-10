# This was AI generated for ease of seeding data and saving time whilist testing. Thank you CHATGPT!

from django.contrib.auth.models import User
from itworkedlocally_app.models import Category, Post, Comment

# Clear existing data (order matters because of FK constraints)
Comment.objects.all().delete()
Post.objects.all().delete()
Category.objects.all().delete()
User.objects.exclude(is_superuser=True).delete()  # keep your admin user

# Users
users = {
    "alex": "Bv3!qN7#tP2@kL8$zR5^mD1*",
    "jordan": "X9@rT6!pQ2#hV7$yN4^sK8%",
    "sam": "M7#dP2@xL9!qW5$zR1^tH6&",
    "mod": "C8!nR3@pT7#kV2$yQ9^sL5*",
    "bytebender": "Q3#vH8!mT2@xN6$kR9^pL1&",
    "kernel_kate": "T9!qP4@dR7#xV2$kN6^mH8*",
    "devnull_dan": "R6@kN2#tP9!xQ3$hV7^mL1&",
    "nginx_nate": "P2!xT8@qR5#kN9$hV3^mL6&",
    "sql_sorcerer": "N7#hV2@pT9!xQ3$kR6^mL1&",
    "react_riley": "V5!kR2@pT9#xQ3$hN7^mL1&",
    "docker_drew": "T8#xQ3!kR6@pN2$hV9^mL1&",
    "cipher_chloe": "Q9!hV3@pT7#xR2$kN6^mL1&",
    "ops_oliver": "R4#kN8!xT2@pQ9$hV6^mL1&",
    "linux_lena": "N2@pT9#xQ3!kR6$hV7^mL1&",
    "api_aria": "T7!xQ3@pR6#kN2$hV9^mL1&",
    "bughunter_ben": "V9#hN2!pT7@xQ3$kR6^mL1&",
    "stacktrace_syd": "Q2!xT8@pR6#kN9$hV3^mL7&",
    "commit_cora": "R9#kN2!xT7@pQ3$hV6^mL1&",
    "cloud_cameron": "T6!xQ3@pR9#kN2$hV7^mL1&",
    "packet_paul": "N9#hV2!pT7@xQ3$kR6^mL1&",
}

created_users = {}
for username, password in users.items():
    if username == "mod":
        created_users[username] = User.objects.create_user(
            username=username,
            password=password,
            is_staff=True
        )
    else:
        created_users[username] = User.objects.create_user(username=username, password=password)

# Categories (tech forum style)
categories = {
    "Windows": None,
    "Linux": None,
    "Web Development": None,
    "Hardware": None,
    "DevOps": None,
    "Networking": None,
    "Security": None,
    "Databases": None,
    "Cloud": None,
    "Programming": None,
    "Game Development": None,
}

created_categories = {}
for name in categories.keys():
    created_categories[name] = Category.objects.create(name=name)

# Posts
posts = [
    # Windows
    dict(
        category="Windows",
        title="Windows 11 Wi-Fi keeps disconnecting every 10 minutes",
        author="alex",
        body=(
            "Wi-Fi drops randomly under normal browsing and sometimes under download. "
            "Already rebooted, updated Windows, and restarted router. "
            "Device: Alienware Aurora R10 Ryzen Edition. Any troubleshooting checklist?"
        ),
        repo_url=""
    ),
    dict(
        category="Windows",
        title="Windows 11: High memory usage by 'Antimalware Service Executable' during builds",
        author="bughunter_ben",
        body=(
            "When running builds (node + python), Defender spikes CPU/RAM and everything crawls. "
            "What exclusions are safe to add for dev folders without disabling protection?"
        ),
        repo_url=""
    ),
    dict(
        category="Windows",
        title="WSL2: 'The virtual machine could not be started because a required feature is not installed'",
        author="react_riley",
        body=(
            "Trying to enable WSL2 on Windows 11. WSL installs but distro won't start. "
            "Hyper-V / Virtual Machine Platform options are enabled. What else should I check?"
        ),
        repo_url=""
    ),
    dict(
        category="Windows",
        title="Windows 11: Bluetooth headphones crackling when microphone is active",
        author="kernel_kate",
        body=(
            "Audio is fine until a call/app uses the mic. Then output quality drops and crackles. "
            "Is there a fix besides buying a separate mic or switching to wired?"
        ),
        repo_url=""
    ),

    # Linux
    dict(
        category="Linux",
        title="Ubuntu: permission denied when running a script with ./deploy.sh",
        author="jordan",
        body=(
            "I wrote a bash script but running `./deploy.sh` returns permission denied. "
            "What’s the correct fix and what common pitfalls should I check?"
        ),
        repo_url=""
    ),
    dict(
        category="Linux",
        title="Linux: systemd service keeps restarting and shows 'Exec format error'",
        author="devnull_dan",
        body=(
            "Created a systemd service for a binary, but it loops restarting with Exec format error. "
            "Binary runs manually. What causes this (arch, shebang, permissions)?"
        ),
        repo_url=""
    ),
    dict(
        category="Linux",
        title="Ubuntu: apt update failing with 'NO_PUBKEY' after adding a third-party repo",
        author="linux_lena",
        body=(
            "Added a repo and now `apt update` fails with NO_PUBKEY. "
            "What's the correct way to add keys now that apt-key is deprecated?"
        ),
        repo_url=""
    ),
    dict(
        category="Linux",
        title="NVIDIA on Ubuntu: external monitor not detected after driver update",
        author="ops_oliver",
        body=(
            "After updating NVIDIA drivers, my HDMI monitor doesn't show up. "
            "Xorg vs Wayland confusion. What steps should I try to restore display output?"
        ),
        repo_url=""
    ),

    # Web Development
    dict(
        category="Web Development",
        title="Django REST API returns 403 CSRF failed in Postman with TokenAuth",
        author="sam",
        body=(
            "Testing DRF endpoints in Postman and getting CSRF errors on POST/PUT. "
            "Using TokenAuthentication. What settings/middleware/auth classes should be used?"
        ),
        repo_url=""
    ),
    dict(
        category="Web Development",
        title="React: state updates not reflected immediately after setState/useState",
        author="react_riley",
        body=(
            "I'm logging state right after calling setState/useState setter and it's the old value. "
            "What's the correct pattern to run code after state updates?"
        ),
        repo_url=""
    ),
    dict(
        category="Web Development",
        title="CORS error when frontend calls /api behind nginx reverse proxy",
        author="nginx_nate",
        body=(
            "Frontend served by nginx, backend is Django. Browser blocks requests with CORS errors. "
            "What headers should be set and where (nginx vs Django) for token auth + JSON?"
        ),
        repo_url=""
    ),
    dict(
        category="Web Development",
        title="Fetch API: handling non-JSON error responses without crashing parsing",
        author="api_aria",
        body=(
            "My fetch helper does response.json(), but when backend returns HTML/plaintext error, it throws. "
            "What's a robust pattern to handle JSON vs non-JSON responses?"
        ),
        repo_url=""
    ),

    # Hardware
    dict(
        category="Hardware",
        title="Laptop overheating after cleaning fans and replacing thermal paste",
        author="jordan",
        body=(
            "Cleaned the fan and replaced thermal paste, but temps are still high under load. "
            "Any checklist to diagnose (heatsink seating, fan curve, sensors, undervolt)?"
        ),
        repo_url=""
    ),
    dict(
        category="Hardware",
        title="PC random reboots under GPU load with no BSOD",
        author="bytebender",
        body=(
            "Gaming or running benchmarks causes sudden reboot, no blue screen. "
            "Event Viewer shows Kernel-Power 41. Is this PSU, GPU, thermals, or RAM?"
        ),
        repo_url=""
    ),
    dict(
        category="Hardware",
        title="New NVMe SSD not detected in BIOS but shows in Windows sometimes",
        author="stacktrace_syd",
        body=(
            "Installed NVMe in M.2 slot. BIOS doesn't always show it, Windows intermittently does. "
            "Could this be lane sharing, BIOS setting, or a bad drive?"
        ),
        repo_url=""
    ),

    # DevOps
    dict(
        category="DevOps",
        title="Docker Compose: Django can't connect to Postgres (could not translate host name db)",
        author="alex",
        body=(
            "Django container can’t resolve DB hostname. Using docker compose with services `api` and `db`. "
            "What are the common causes (networks, env vars, container startup timing)?"
        ),
        repo_url=""
    ),
    dict(
        category="DevOps",
        title="Nginx reverse proxy: 413 Request Entity Too Large on file upload",
        author="nginx_nate",
        body=(
            "Uploading images/files returns 413. "
            "Where do I set client_max_body_size and do I need to change app server settings too?"
        ),
        repo_url=""
    ),
    dict(
        category="DevOps",
        title="Gunicorn workers and timeouts: API requests hang under moderate load",
        author="ops_oliver",
        body=(
            "Django behind gunicorn + nginx. Under load, requests queue and time out. "
            "How should I size workers/threads and set proxy/read timeouts?"
        ),
        repo_url=""
    ),
    dict(
        category="DevOps",
        title="Docker: container time drift causes JWT/Token auth failures",
        author="cipher_chloe",
        body=(
            "Some users get token failures that disappear after restart. "
            "Is container time drift a thing and how do I ensure correct time sync?"
        ),
        repo_url=""
    ),

    # Networking
    dict(
        category="Networking",
        title="DNS resolves slowly on home network but fine on mobile hotspot",
        author="packet_paul",
        body=(
            "Pages stall on first load, then fast after. Switching to hotspot fixes it. "
            "How to diagnose DNS latency (router, ISP DNS, local caching)?"
        ),
        repo_url=""
    ),
    dict(
        category="Networking",
        title="Port forwarding works for HTTP but not for SSH on same host",
        author="packet_paul",
        body=(
            "Forwarded 80 and 22 to a LAN host. HTTP works externally, SSH times out. "
            "What should I check (ISP blocks, router rules, host firewall, fail2ban)?"
        ),
        repo_url=""
    ),
    dict(
        category="Networking",
        title="Nginx behind Cloudflare: real client IP not showing in logs",
        author="cloud_cameron",
        body=(
            "All logs show Cloudflare IPs. Need real user IP for rate limiting. "
            "What headers and nginx directives should be used (real_ip, CF-Connecting-IP)?"
        ),
        repo_url=""
    ),

    # Security
    dict(
        category="Security",
        title="Token authentication: should I store auth token in localStorage or cookies",
        author="cipher_chloe",
        body=(
            "SPA frontend calling a Django API using token auth. "
            "What are the risks of localStorage vs httpOnly cookies and how to mitigate XSS/CSRF?"
        ),
        repo_url=""
    ),
    dict(
        category="Security",
        title="SSH hardening for VPS: best practices without locking myself out",
        author="ops_oliver",
        body=(
            "I want to harden SSH (keys only, disable root, change port, fail2ban). "
            "What's the safe order of operations to avoid getting locked out?"
        ),
        repo_url=""
    ),
    dict(
        category="Security",
        title="Nginx: rate limiting API endpoints without breaking logged-in users",
        author="nginx_nate",
        body=(
            "Need to limit abusive traffic on /api. "
            "How do I configure nginx rate limiting for unauthenticated traffic while keeping normal users OK?"
        ),
        repo_url=""
    ),

    # Databases
    dict(
        category="Databases",
        title="PostgreSQL: slow query after adding index (planner chooses seq scan)",
        author="sql_sorcerer",
        body=(
            "Added index but EXPLAIN still shows sequential scan. "
            "What factors cause planner to ignore index (stats, selectivity, type casts)?"
        ),
        repo_url=""
    ),
    dict(
        category="Databases",
        title="Django migrations: duplicate column error after merge conflict",
        author="commit_cora",
        body=(
            "Two branches added migrations and now applying migrations causes duplicate column/table errors. "
            "What’s the correct workflow to fix migration history cleanly?"
        ),
        repo_url=""
    ),
    dict(
        category="Databases",
        title="Postgres in Docker: data disappears after container rebuild",
        author="docker_drew",
        body=(
            "Rebuilding containers resets the DB. I thought volumes persist. "
            "What common mistakes cause data loss (named volumes, bind mounts, compose changes)?"
        ),
        repo_url=""
    ),

    # Cloud
    dict(
        category="Cloud",
        title="VPS nginx reverse proxy to Docker: 502 Bad Gateway after deploy",
        author="cloud_cameron",
        body=(
            "After pulling latest code and restarting docker compose, nginx returns 502. "
            "What steps to debug (upstreams, ports, container health, logs)?"
        ),
        repo_url=""
    ),
    dict(
        category="Cloud",
        title="Let's Encrypt renewal failing after moving site behind reverse proxy",
        author="cloud_cameron",
        body=(
            "Certbot renew fails with HTTP-01 challenge errors since switching to reverse proxy setup. "
            "How should /.well-known be routed and what ports must be open?"
        ),
        repo_url=""
    ),
    dict(
        category="Cloud",
        title="Dockerized app on VPS: disk space slowly fills up over weeks",
        author="ops_oliver",
        body=(
            "VPS disk usage increases steadily. Suspect docker images, logs, volumes. "
            "What commands and policies should I use to manage disk growth safely?"
        ),
        repo_url=""
    ),

    # Programming
    dict(
        category="Programming",
        title="Python: requests timeout vs connection timeout and retry strategy",
        author="api_aria",
        body=(
            "Calling third-party APIs. Confused about timeouts and retries. "
            "What’s the correct way to set connect/read timeouts and implement backoff retries?"
        ),
        repo_url=""
    ),
    dict(
        category="Programming",
        title="JavaScript: debounce vs throttle for search suggestions API calls",
        author="bytebender",
        body=(
            "Typing in a search box triggers many calls. "
            "When should I debounce vs throttle and what's a clean implementation?"
        ),
        repo_url=""
    ),
    dict(
        category="Programming",
        title="Git: accidentally committed secrets, how to remove from history properly",
        author="cipher_chloe",
        body=(
            "A .env or API key got committed. Removed in latest commit but it's still in history. "
            "How do I purge it and rotate safely?"
        ),
        repo_url=""
    ),

    # Game Development
    dict(
        category="Game Development",
        title="Unity: stuttering every few seconds despite stable FPS counter",
        author="bytebender",
        body=(
            "FPS shows stable but gameplay stutters. "
            "What profiling steps should I take (GC allocs, spikes, vsync, background tasks)?"
        ),
        repo_url=""
    ),
    dict(
        category="Game Development",
        title="Godot: input feels delayed on fullscreen compared to windowed mode",
        author="stacktrace_syd",
        body=(
            "Noticeable input lag in fullscreen. "
            "How do I reduce latency (vsync, frame pacing, physics ticks) and verify improvements?"
        ),
        repo_url=""
    ),
    dict(
        category="Game Development",
        title="OpenGL: black screen after compiling shaders with no errors",
        author="devnull_dan",
        body=(
            "Shader compile/link says OK, but render is black. "
            "What checklist should I run (VAO/VBO binding, glUseProgram, uniforms, depth test)?"
        ),
        repo_url=""
    ),
]

# SEO-friendly, StackOverflow-like topics
posts += [
    dict(
        category="Programming",
        title="Python: ModuleNotFoundError after pip install (venv vs system python confusion)",
        author="linux_lena",
        body=(
            "Installed a package with pip, but running the script still shows ModuleNotFoundError. "
            "How do I confirm which python/pip is being used and fix venv activation issues?"
        ),
        repo_url=""
    ),
    dict(
        category="Web Development",
        title="React Router: direct refresh on /post/123 returns 404 behind nginx",
        author="nginx_nate",
        body=(
            "SPA routes work when navigating in-app, but refreshing a deep link returns 404. "
            "What nginx try_files config is needed for client-side routing?"
        ),
        repo_url=""
    ),
    dict(
        category="DevOps",
        title="Docker Compose: environment variables not loading from .env file",
        author="docker_drew",
        body=(
            ".env exists but variables are empty inside containers. "
            "What's the correct placement/naming and how does compose resolve env files?"
        ),
        repo_url=""
    ),
    dict(
        category="Databases",
        title="PostgreSQL: connection pool exhausted in Django under concurrent requests",
        author="sql_sorcerer",
        body=(
            "Under load, requests fail with too many connections. "
            "How should I tune Django, gunicorn, and Postgres max_connections / pooling?"
        ),
        repo_url=""
    ),
    dict(
        category="Security",
        title="JWT authentication: token expires mid-session, best refresh token approach",
        author="api_aria",
        body=(
            "Users stay logged in for hours and access token expires. "
            "What's a secure refresh token flow for SPAs and APIs?"
        ),
        repo_url=""
    ),
    dict(
        category="Networking",
        title="Home network: VLAN setup breaks Chromecast and local discovery",
        author="packet_paul",
        body=(
            "Moved IoT devices to a VLAN and now casting/discovery doesn't work. "
            "What protocols are involved (mDNS/SSDP) and how to route/reflect them safely?"
        ),
        repo_url=""
    ),
    dict(
        category="Windows",
        title="Windows: USB devices disconnect under load (power management/USB selective suspend)",
        author="alex",
        body=(
            "Keyboard/mouse/USB drive drop randomly, especially during gaming. "
            "What power settings and chipset drivers should I check?"
        ),
        repo_url=""
    ),
    dict(
        category="Linux",
        title="Linux: journald logs growing too large and filling disk",
        author="ops_oliver",
        body=(
            "Disk usage increases and /var/log/journal is huge. "
            "How to configure retention/limits and safely vacuum logs?"
        ),
        repo_url=""
    ),
]

posts.append(
    dict(
        category="Programming",
        title="Check out this GitHub Repo!",
        author="bytebender",
        body=(
            "We are testing the GitHub and Stack Overflow API functionality here. "
            "This repository explores GitHub Achievements, profile gamification, "
            "badges, and contribution insights. Perfect for experimenting with "
            "API integrations, metadata parsing, and related StackOverflow lookups.\n\n"
            "Specifically testing:\n"
            "- GitHub repository metadata extraction\n"
            "- Stars, issues, and last updated timestamps\n"
            "- Related StackOverflow question mapping\n\n"
            "If the integration works properly, we should see real repo data and "
            "relevant StackOverflow entries rendered dynamically."
        ),
        repo_url="https://github.com/gomzyakov/github-achievements"
    )
)

# Create 36 posts 
posts = posts[:46]

for p in posts:
    Post.objects.create(
        category=created_categories[p["category"]],
        title=p["title"],
        author=created_users[p["author"]],
        body=p["body"],
        repo_url=p["repo_url"]
    )

exit()