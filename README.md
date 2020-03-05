# Atlas bug generator
Simple utility for generating random bug reports for internal project.

# Usage
```
> python gen.py 5
- user which is both vendor and VRM is able to delegate to vendor users
- vendor can delegate proxied requests
- guest vendor cannot be notified by same-company users
- admin cannot access draft requests
- guest user doesn't have permission to copy master form to unsent questionnaires
```
