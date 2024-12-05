import python


from StrConst s
where
  // Check if the string contains keywords like "password" or "pwd"
  s.getValue().regexpMatch("(?i).*\\b(password|pwd|passwd)\\b.*") and
  // Exclude empty strings
  not s.getValue() = ""
select s, "Avoid using plaintext passwords in your code. Consider using environment variables or a secure secrets management system."
