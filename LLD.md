# Low-Level Design (LLD)
## Project: LeetCode-Solutions

**Repository:** https://github.com/ankitsharma06102007-gif/LeetCode-Solutions  
**Document version:** 1.0

---

## 1. Purpose

This document defines practical conventions for individual problem folders and solution files. It describes how a contributor should add, review, and maintain a DSA solution.

Because the repository is a collection of independent solutions, its low-level design is based on file organization and a repeatable problem-solving workflow rather than classes, APIs, database tables, or service interfaces.

## 2. Problem Unit

A **problem unit** is the smallest independently maintainable part of the repository. It represents one coding challenge and contains its implementation plus optional notes or tests.

Recommended layout:

```text
<problem-folder>/
├── solution.<extension>
├── README.md                 # optional problem explanation
└── tests/                    # optional, when useful
    └── test-cases.<extension>
```

Use the actual language extension for the implementation. Do not create empty optional files solely to match this example.

## 3. Naming Conventions

- Prefer a folder name that includes the platform problem ID when one exists and a short readable problem name.
- Use lowercase words separated by hyphens for folder names.
- Use a clear filename such as `solution.py`, `solution.cpp`, or the relevant language equivalent.
- Keep one problem's implementation separate from another problem's implementation.
- Avoid names such as `final2`, `newest`, or `test-final`.

The currently visible folder `0412-fizz-buzz` is an example of an ID-and-name style.

## 4. Solution File Responsibilities

A solution file should:
1. implement the required algorithm;
2. follow the input/output contract expected by the problem or judge;
3. use meaningful variable and function names;
4. handle relevant boundary conditions;
5. avoid unrelated application logic; and
6. contain only comments that clarify non-obvious decisions.

Where the platform supplies a required function signature, preserve that signature.

## 5. Problem Explanation Template

When adding a problem-level `README.md`, use this suggested structure:

```markdown
# <Problem Name>

- Platform: <LeetCode / GFG / HackerRank / other>
- Problem ID: <ID, if available>
- Difficulty: <Easy / Medium / Hard, if known>
- Topic: <Array / String / Hashing / ...>

## Problem Summary
Explain the task in your own words.

## Approach
Describe the algorithm and why it works.

## Complexity
- Time: O(...)
- Space: O(...)

## Edge Cases
- <Relevant boundary case>
- <Another relevant case>
```

Only include facts that have been checked against the actual problem statement and implementation.

## 6. Algorithm Design Workflow

For each problem:

1. **Read:** Identify input, output, constraints, and examples.
2. **Analyze:** Look for a direct approach and possible improvements.
3. **Choose:** Select a suitable data structure and algorithm.
4. **Implement:** Write the solution using the platform's expected interface.
5. **Verify:** Check the supplied examples and relevant edge cases.
6. **Explain:** Record the approach and complexity when useful.
7. **Commit:** Save the completed change with a descriptive Git commit.

## 7. Testing Guidelines

At minimum, verify:
- the provided sample input and expected output;
- the smallest valid input;
- boundary values allowed by the constraints;
- repeated values, empty collections, or negative values when applicable; and
- a typical case that exercises the main algorithm.

Testing should match the problem's actual constraints. Not every category applies to every problem.

If a local test file is added, keep test data and test instructions close to the relevant problem. Do not claim automated test coverage unless tests are actually present and run.

## 8. Complexity Analysis

For each solution, estimate:
- **Time complexity:** how the number of operations grows with input size;
- **Space complexity:** how much additional memory the algorithm uses.

State the variables used in the analysis (for example, `n` for the number of elements). Distinguish auxiliary space from input storage when relevant.

## 9. Error Prevention and Code Review Checklist

Before committing a solution, confirm:

- [ ] The implementation matches the required function or input/output format.
- [ ] Variable names are understandable.
- [ ] The algorithm handles the relevant edge cases.
- [ ] No unrelated files were modified.
- [ ] The code has been run or checked against appropriate examples.
- [ ] Complexity notes are accurate if included.
- [ ] The folder and file names follow the repository convention.
- [ ] No credentials, personal tokens, or machine-specific paths are committed.

## 10. Git Workflow

Suggested commands:

```bash
git status
git add <problem-folder> PRD.md HLD.md LLD.md
git commit -m "docs: add repository design documents"
git push
```

If only one problem is being added, stage only that problem's files. Review `git status` before committing to avoid including unrelated changes.

## 11. Current Scope and Limitations

- The visible root currently lists `0412-fizz-buzz` and `README.md`.
- The exact implementation language, source file names, and internal folder contents have not been asserted here because they were not confirmed from the accessible repository listing.
- This LLD defines recommended conventions for future additions; adapt it if the existing solution files use a different established pattern.
