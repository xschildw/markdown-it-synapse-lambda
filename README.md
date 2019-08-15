# markdown-it-synapse-lambda
Implement markdown-it-synapse-server as lambda

To deploy:
```bash
cdk deploy --profile <deployer-profile> -c CERT_ARN=<arn_domain_cert> -c DOMAIN_NAME=<custom_domain_name>
```

Then update the DNS record in Route53 to an A-record that's an alias to the API gateway created.

