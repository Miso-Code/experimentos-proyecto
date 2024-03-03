# bin/bash
AWS_REGION="us-east-1"
AWS_ACCOUNT_ID="887664210442"

aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

for d in */; do
    if [ -f $d/Dockerfile ]; then
        d=${d%/}
        echo "Building and pushing $d"
        docker build -t $d $d
        docker tag $d:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$d:latest
        docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$d:latest
    fi
done

echo "All images pushed to ECR"
