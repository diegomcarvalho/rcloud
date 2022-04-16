import streamlit as st
import os

st.title("Cloud System")

status = os.popen("df -h | fgrep Cloud").read()

st.text(status)

remotes = os.popen("rclone listremotes").read().strip().replace("\n", "").split(":")

mnt_remotes = list()
umt_remotes = list()

for i in remotes[:-1]:
    if i in status:
        umt_remotes.append(i)
    else:
        mnt_remotes.append(i)

add_umt_selectbox = st.sidebar.selectbox("Umount a remote", umt_remotes)
buttton_umt = st.sidebar.button("Umount")
add_mnt_selectbox = st.sidebar.selectbox("Mount a remote", mnt_remotes)
buttton_mnt = st.sidebar.button("Mount")

if buttton_umt:
    with st.spinner(f"Umounting {add_umt_selectbox}..."):
        os.system(f"umount {add_umt_selectbox}:")
    st.experimental_rerun()

if buttton_mnt:
    with st.spinner(f"Mounting {add_mnt_selectbox}..."):
        os.system(f"/Users/carvalho/bin/cloudmount {add_mnt_selectbox}")
    st.experimental_rerun()
