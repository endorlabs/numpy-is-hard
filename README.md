# Surviving Dependency Hell: The TensorFlow Upgrade Challenge

## The Challenge

- **Welcome to dependency hell.** One upgrade can break everything.
- Your project needs a security update, but **conflicting dependencies** stand in the way.
- TensorFlow, NumPy, and other libraries all have **strict version requirements**.
- **Your goal:** Reduce conflicts and improve security **without breaking the project.**

## What You Have

- A `requirements.txt` file full of conflicting dependencies.
- TensorFlow, NumPy, and other packages that don't always play nicely together.
- **An OSV scanner to detect vulnerabilities.**
- **15 minutes to minimize conflicts while keeping the project functional.**

## What You Don’t Have

- **A clean upgrade path.**
- **An easy fix.**
- **A guarantee that upgrading one thing won’t break something else.**

## The Process

1. **Set up your environment:**
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Run the OSV Scanner** to check for vulnerabilities:
   ```sh
   pip freeze > requirements.txt  # Ensure dependencies are locked
   ./osv-scanner scan --lockfile requirements.txt
   ```

3. **Upgrade TensorFlow to 2.9.0**:
   ```sh
   pip install tensorflow==2.9.0
   ```
   - **Expect issues** with other dependencies.
   - **Run OSV Scanner again** to check for remaining vulnerabilities.

4. **Upgrade TensorFlow to 2.14.0**:
   ```sh
   pip install tensorflow==2.14.0
   ```
   - **Watch more things break.**
   - **Run OSV Scanner again** after upgrading.

5. **Solve conflicts manually**:
   - **Check error messages**—they often tell you which packages have conflicts.
   - **Modify `requirements.txt`**—try adjusting package versions to find a working set.
   - **Use `pip install --upgrade <package>` carefully**—some dependencies need manual intervention to align with the correct versions.
   - **Look for alternative versions**—sometimes upgrading a package incrementally helps resolve issues.
   - **Check the dependency chain**—a package may depend on an outdated version of another, causing conflicts.
   - **Test frequently**—after each change, verify that your application still works.

6. **The person who reduces vulnerabilities the most in 15 minutes wins.**

## What This Teaches You

- **Dependency hell is real.**
- Security upgrades can introduce **more problems** than they fix.
- **Manifest-based SCA tools** don’t always show the full picture.
- Developers deal with this daily—security needs to understand the struggle before demanding upgrades.

This is a real-world challenge. **Good luck.**
