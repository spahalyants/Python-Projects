# This code shows a list being used as a stack (last in, first out),
# with a real-world analogy of browser history:


browsing_session = []
browsing_session.append("google.com")
browsing_session.append("youtube.com")
browsing_session.append("github.com")

print(browsing_session[-1])  # "github.com" (current page)

browsing_session.pop()       # go back
print(browsing_session[-1])  # "youtube.com" (current page now)

if not browsing_session:
    print("No history left")