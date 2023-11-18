function handler(event) {
  return {
    statusCode: 302,
    headers: {
      location: { value: "https://blog.i-tale.jp/" },
    },
  };
}
