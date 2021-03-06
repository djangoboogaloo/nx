from django import forms


from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)
User=get_user_model()



class userloginform(forms.Form):
	username=forms.CharField()
	password=forms.CharField(widget=forms.PasswordInput)
	def clean(self,*args,**kwargs):
		username=self.cleaned_data.get("username")
		password=self.cleaned_data.get("password")

		# user_qs= User.objects.filter(username=username)
		# if user_qs.count() ==1:
		# 	user=user_qs.first()
		if username and password:
			user=authenticate(username=username,password=password)
			if not user:
				raise forms.ValidationError("something went wrong !")
			if not  user.check_password(password):
				raise forms.ValidationError("something went wrong !")
			if not user.is_active:
				raise forms.ValidationError("need active!")

		return super(userloginform,self).clean(*args,**kwargs)





class userresignform(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model=User
		fields=[
		'username',

		'password',
		]

	
