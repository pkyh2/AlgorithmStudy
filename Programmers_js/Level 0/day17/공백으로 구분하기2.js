const solution = (my_string) => {
  return my_string.split(" ").filter((str) => str !== "");
};

console.log(solution(" i    love  you"));
