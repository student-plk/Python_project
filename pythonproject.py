import streamlit as st
import os

st.set_page_config(page_title="Linux & Docker Menu Tool", layout="centered")

st.title("🖥️ Linux & Docker Menu Tool - Command Dashboard")
st.markdown("Run your favorite Linux, Docker, and Windows commands from a single interface using SSH.")

# SSH Credentials Section
st.sidebar.header("🔐 SSH Login")
username = st.sidebar.text_input("Linux Username", placeholder="e.g. root")
remote_ip = st.sidebar.text_input("Remote Linux IP", placeholder="e.g. 192.168.1.10")
ssh_ready = username and remote_ip

def run_ssh_command(cmd):
    if not ssh_ready:
        st.error("Please enter SSH credentials in the sidebar.")
        return
    full_cmd = f'ssh {username}@{remote_ip} "{cmd}"'
    st.write(f"🔧 Running: `{cmd}`")
    result = os.popen(full_cmd).read()
    st.code(result)

# Tabs
tab1, tab2, tab3 = st.tabs(["🐧 Linux Commands", "🐳 Docker Commands", "🪟 Windows Commands"])

# ------------------- Linux -------------------
with tab1:
    st.subheader("Basic Linux Commands")

    linux_cmds = {
        "📅 Date": "date",
        "📆 Calendar": "cal",
        "🌐 ifconfig": "ifconfig",
        "📂 List Files": "ls",
        "📍 Present Directory": "pwd",
        "🧽 Remove File": "rm",
        "🗑️ Remove Directory": "rmdir",
        "📁 Make Directory": "mkdir",
        "📝 Create File": "touch newfile.txt",
        "🧨 Remove Force": "rm -rf temp",
        "📄 Cat File": "cat newfile.txt",
        "🔌 Ping Google": "ping -c 4 google.com",
        "💿 Disk Usage": "df -h",
        "🔍 Who am I": "whoami",
        "📜 History": "history",
        "📦 Yum Install Apache": "yum install httpd -y",
        "▶️ Start Apache": "systemctl start httpd",
        "⛔ Stop Firewall": "systemctl stop firewalld",
    }

    for label, command in linux_cmds.items():
        if st.button(label):
            run_ssh_command(command)

# ------------------- Docker -------------------
with tab2:
    st.subheader("Docker Commands")

    docker_cmd = st.selectbox("Choose Docker Command", [
        "Run Container",
        "Start Container",
        "Stop Container",
        "Attach Container",
        "Remove Container",
        "List Images",
        "List All Containers"
    ])

    if docker_cmd == "Run Container":
        name = st.text_input("Container Name")
        image = st.text_input("Image Name")
        if st.button("Run Container"):
            run_ssh_command(f"docker run -dit --name {name} {image}")
    elif docker_cmd == "Start Container":
        name = st.text_input("Container Name")
        if st.button("Start"):
            run_ssh_command(f"docker start {name}")
    elif docker_cmd == "Stop Container":
        name = st.text_input("Container Name")
        if st.button("Stop"):
            run_ssh_command(f"docker stop {name}")
    elif docker_cmd == "Attach Container":
        name = st.text_input("Container Name")
        if st.button("Attach"):
            run_ssh_command(f"docker attach {name}")
    elif docker_cmd == "Remove Container":
        name = st.text_input("Container Name")
        if st.button("Remove"):
            run_ssh_command(f"docker rm {name}")
    elif docker_cmd == "List Images":
        if st.button("Show Docker Images"):
            run_ssh_command("docker images")
    elif docker_cmd == "List All Containers":
        if st.button("Show All Containers"):
            run_ssh_command("docker ps -a")

# ------------------- Windows -------------------
with tab3:
    st.subheader("Windows Local Actions")

    if st.button("Open id_rsa.pub"):
        os.system("notepad id_rsa.pub")
        st.success("Opened id_rsa.pub in Notepad.")

    if st.button("Open pp.py"):
        os.system("notepad pp.py")
        st.success("Opened pp.py in Notepad.")

    if st.button("Open menu.html"):
        os.system("notepad menu.html")
        st.success("Opened menu.html in Notepad.")

    with st.expander("📲 Send WhatsApp Message Instantly"):
        phone = st.text_input("Phone Number (with +91)")
        msg = st.text_input("Message")
        if st.button("Send WhatsApp Message"):
            os.system(f"python -c \"import pywhatkit; pywhatkit.sendwhatmsg_instantly('{phone}', '{msg}')\"")
            st.success("Message Sent via pywhatkit!")

    with st.expander("👥 Send WhatsApp Group Message"):
        if st.button("Send Group Msg"):
            os.system("python -c \"import pywhatkit; pywhatkit.sendwhatmsg_to_group_instantly('team 38', 'hello')\"")
            st.success("Group Message Sent")

