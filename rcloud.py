import streamlit as st
import os

st.header("Dashboard")


st.subheader("VPN Subsystem Status")

status = os.popen("/Users/carvalho/bin/vpn status").read()
vpn_status = False
if "Yes" in status:
    vpn_status = True
    st.text("VPN is RUNNING")
else:
    vpn_status = False
    st.text("VPN is NOT running")

st.subheader("Cloud Status")

status = os.popen("df -h | fgrep Cloud").read()

if len(status) == 0:
    st.text("None remote mounted.")
else:
    st.text(status)

remotes = os.popen("rclone listremotes").read().strip().replace("\n", "").split(":")

mnt_remotes = list()
umt_remotes = list()

for i in remotes[:-1]:
    if i in status:
        umt_remotes.append(i)
    else:
        mnt_remotes.append(i)


if vpn_status:
    vpn_button = st.sidebar.button("VPN OFF")
else:
    vpn_button = st.sidebar.button("VPN ON")

st.sidebar.markdown("---")

add_umt_selectbox = st.sidebar.selectbox("Umount a remote", umt_remotes)
button_umt = st.sidebar.button("Umount")
add_mnt_selectbox = st.sidebar.selectbox("Mount a remote", mnt_remotes)
button_mnt = st.sidebar.button("Mount")


if button_umt:
    with st.spinner(f"Umounting {add_umt_selectbox}..."):
        os.system(f"umount {add_umt_selectbox}:")
    st.experimental_rerun()

if button_mnt:
    with st.spinner(f"Mounting {add_mnt_selectbox}..."):
        os.system(f"/Users/carvalho/bin/cloudmount {add_mnt_selectbox}")
    st.experimental_rerun()

if vpn_button:
    if vpn_status:
        os.system("/Users/carvalho/bin/vpn off")
        st.experimental_rerun()
    else:
        os.system("/Users/carvalho/bin/vpn on")
        st.experimental_rerun()
