const { Octokit } = require("@octokit/rest");
const chalk = require("chalk");

const username = process.argv[2];
const octokit = new Octokit({ auth: process.env.GITHUB_TOKEN });

(async () => {
  const { data } = await octokit.users.getByUsername({ username });
  console.log(chalk.blue(`User: ${data.login}`));
  console.log(`Followers: ${data.followers}`);
  console.log(`Public repos: ${data.public_repos}`);
  console.log(`Created at: ${data.created_at}`);
})();
