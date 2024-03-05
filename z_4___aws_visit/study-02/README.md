![alt text](images/markdown-image.png)
![alt text](images/markdown-image-1.png)




# pollyroll
![alt text](images/markdown-image-2.png)
```json  
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Action": [
				"dynamodb:DeleteItem",
				"dynamodb:PutItem",
				"dynamodb:GetItem",
				"dynamodb:Query",
				"dynamodb:Scan",
				"dynamodb:UpdateItem",
				"dynamodb:DescribeTable",
				"polly:SynthesizeSpeech",
				"s3:PutObject",
				"s3:GetObject",
				"logs:CreateLogGroup",
				"logs:CreateLogStream",
				"logs:PutLogEvents",
				"lambda:TagResource"
			],
			"Resource": "*",
			"Effect": "Allow"
		}
	]
}
```