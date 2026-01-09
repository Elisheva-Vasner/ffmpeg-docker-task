package strongPassword;

import java.util.HashMap;
import java.util.Map;

public class StrongPassword {
	
	
	public static boolean MinimumLength(String pass)
	{
		return pass.length()>=8;
	}
	
	public static boolean strongPassword(String pass)
	{
		boolean hasLower = false ;
		boolean hasUpper = false;
		boolean hasDigit = false ;
		boolean hasSpecial = false ;
		int[] duplicates = new int[256];
		int mone=1;
		char prev=0;
		if(!MinimumLength(pass))
			return false;
		for (int i = 0; i < pass.length(); i++)
		{
			char c=pass.charAt(i);
			if(Character.isLowerCase(c)) hasLower=true;
			if(Character.isUpperCase(c)) hasUpper=true;
			if(Character.isDigit(c)) hasDigit=true;
			if(!Character.isLetterOrDigit(c)) hasSpecial=true;
			duplicates[c]++;
			if(duplicates[c]>2)
				return false;

			if(i>0)
			{
				if(c==prev+1)
				{
					mone++;
					if(mone==3)
						return false;
				}
				else
					mone=1;			
			}
			prev=c;
		}
	
		return hasLower && hasUpper && hasDigit &&hasSpecial;
	}
	public static void main(String[] args) {
	
		System.out.println(strongPassword("ab'aA12jk8"));
	

	}

}
