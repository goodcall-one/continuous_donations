# Do good while being awesome
**Automate impact — Integrate donations seamlessly into your GitHub workflows** 

[<img src="logo.png" align="right" width="250">](https://github.com/goodcall-one/github_action)
We provide a GitHub Action for donating to handpicked and verified projects within your development workflow using our own API [Goodcall.one](https://www.goodcall.one/). 

Goodcall.one empowers software companies to make a positive impact through seamless donations, directly tied to their development and business processes. Our easy-to-use API, GitHub workflows, and Slack App allow businesses to integrate charitable giving into their everyday workflows, from product purchases to user engagement. Whether it’s rounding up transactions or donating a percentage of sales, you can support meaningful projects and causes without interrupting your core operations. <br>  <br>

## Possible workflows
* pull requests
* pushes
* _you choose_

## How to get started

1. First, you need to sign up at goodcall.one and create an organization. After that, an Organization Id and an API key are issued. The API key is your secret authentication key and you should **not add it to your workfile yaml files**.

2. Now it's time to create your first wallet, a place where the pledged donations are being stored. When creating a wallet you can pick the project of your choice. All projects are handpicked and verified. After creating a wallet, a Wallet Id is issued.

3. Next you will need to add your API key as a secret in your repository `Settings` -> `Secrets` -> `New Repository Secret`: Name: `donation_apikey`, Value: `<your API key>`. You can also add it as an organization-wide secret in the setting of your organization.

4. Finally you need to update your own repository. Copy one of the example workflows to `<your_git_repository>/.github/workflow` folder, change the file extension to `.yaml`, and update the variables in the workflow to your data. Make sure to set the `test` variable to `true` in order to test your implementation. Push your changes to GitHub and check the GitHub Action tab of your project. If you use GitHub Action for the first time, activate it when prompted.

5. After you set the `test` variable to `false` and run the workflow ones you can verify the number of pledged donations on the dedicated wallet and the dashboard page. At the end of each month, you will receive a bill with the pledged donations for each project and the service fee.

### Example workflow

```yaml
name: Example Integration on Pull Request
on: 
  pull_request_target:
    branches:
      - main
    types:
      - closed
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Donate
        if: github.event.pull_request.merged == true
        id: donate
        uses: goodcall-one/github_action@main
        with:
        # Enter your API variables below
            apikey: ${{ secrets.donation_apikey }}
            organization_id: "<Organization Id>"
            user: ${{ github.actor }}
            wallet_id: "<Dedicated Wallet Id>"
            test: "false"

      - name: Response of goodcall.one API
        run: |
            echo "${{ steps.donate.outputs.response }}"
```

---
### Inputs

| Input            | Description                           |
|------------------|---------------------------------------|
| `apikey`         | Your API key to the Goodcall.one API. |
| `organization_id`   | The Id of your organization.                |
| `user`           | The end user by whom the donation was pleaded. The default is your GitHub user name. |
| `wallet_id`      | Id of the wallet in which a dedicated project is selected..    |
| `test`     | Set `true` to test the workflow without pleading for a donation. |

### Outputs

| Output           | Description                           |
|------------------|---------------------------------------|
| `response`       | JSON response of the Goodcall.one API |

