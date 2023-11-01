function handler(event) {
  var response = {
      statusCode: 302,
      statusDescription: 'Found',
      headers: {
          'location': { value: 'https://blog.i-tale.jp/' }
      }
  };
  return response;
}
