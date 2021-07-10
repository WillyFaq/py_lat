import speedtest

st = speedtest.Speedtest()
dow = st.download()
upl = st.upload()
print("Your Download Speed is ", dow//10**6," Mbps")
print("Your Upload Speed is ", upl//10**6," Mbps")
print("Your Ping is ", int(st.results.ping)," ms")
# print("Your Download Speed is ", st.download()," Mbps")
# print("Your Upload Speed is ", st.upload()," Mbps")
# print("Your Download Speed is ", st.download()/100*6," Mbps")
# print("Your Upload Speed is ", st.upload()/100*6," Mbps")
