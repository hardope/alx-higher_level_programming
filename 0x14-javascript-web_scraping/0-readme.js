#!/usr/bin/node
// Reads and prints from file

const argv = process.argv;
FileSystem.readFile(argv[2], 'utf8', () => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
