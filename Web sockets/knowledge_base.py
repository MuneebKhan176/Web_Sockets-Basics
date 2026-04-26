# ---------- Knowledge Base ----------
knowledge_base = [

# ================= BUY PROPERTY =================
(["buy property not working", "buy property", "buy_property function," ,"buying property", "cannot buy property", "purchase failed"],
 "A property purchase can fail for several reasons. The most common are: the property is no longer available, "
 "the buyer does not have enough balance to cover the total cost, or ownership information is inconsistent. "
 "In many systems, additional costs such as commissions or fees are also included, which users often overlook."),

(["property not available", "already sold", "cannot find property"],
 "If a property cannot be bought, it may no longer be available for sale. Systems typically allow purchases only "
 "when the property status is active and marked as available."),

(["insufficient balance buy", "not enough money property"],
 "When buying a property, the system usually checks the total cost, not just the listed price. "
 "Additional fees or commissions may increase the final amount required."),

(["buy own property", "cannot buy my own property"],
 "Most systems prevent users from buying their own property to maintain transaction integrity and avoid invalid operations."),

# ================= TRANSFER =================
(["transfer not working", "money not transferred", "transaction failed"],
 "Transfers typically fail when the sender does not have enough balance, when the receiver does not exist, "
 "or when invalid values are used. Systems verify both accounts before completing the transaction."),

(["transfer same account", "cannot transfer to self"],
 "Transferring money to the same account is usually blocked to prevent redundant or meaningless transactions."),

(["negative transfer amount", "invalid transfer amount"],
 "Transfers require a positive amount. Negative or zero values are generally rejected to maintain financial correctness."),

# ================= WITHDRAW =================
(["withdraw not working", "cannot withdraw"],
 "Withdrawals usually fail when the requested amount exceeds the available balance or when the account cannot be found."),

(["withdraw negative", "invalid withdraw amount"],
 "Withdrawal amounts must be positive. Systems reject invalid or negative values to avoid corruption of balances."),

# ================= DEPOSIT =================
(["deposit not updating", "balance not increasing"],
 "If a deposit does not reflect, it is often due to a failure in saving updated data or an issue during the file update process."),

(["deposit wrong amount", "incorrect deposit"],
 "Incorrect deposit results may occur if input values are not properly formatted or parsed by the system."),

# ================= ACCOUNT / USER =================
(["user not found", "invalid user id"],
 "This issue occurs when the system cannot locate a matching user record. It may be due to incorrect ID input or missing data."),

(["duplicate email", "email already exists"],
 "Most systems prevent duplicate accounts using the same email to maintain uniqueness and avoid conflicts."),

(["login issue", "cannot login"],
 "Login problems typically arise when credentials do not match stored records or when the account does not exist."),

(["profile not updating", "update failed"],
 "Profile updates may fail if the system cannot rewrite the stored data or if there are conflicts like duplicate emails."),

# ================= FILE / DATABASE =================
(["file not found", "database missing"],
 "Many systems rely on external files. If a required file is missing or incorrectly placed, operations depending on it will fail."),

(["data not saving", "changes not persisting"],
 "If changes are not saved, it is usually due to issues in writing back to storage, such as file permissions or incorrect overwrite logic."),

(["corrupted data", "invalid data format"],
 "Corrupted or improperly formatted data can break system operations, especially when numeric values are expected."),

(["empty results", "no data found"],
 "This can happen when no matching records exist or when filters applied are too restrictive."),

# ================= PROPERTY LISTING =================
(["list property not working", "cannot list property"],
 "Listing a property may fail if the property does not exist, the user does not own it, or it is already listed."),

(["invalid agent", "agent not found"],
 "If an agent is required for listing, the system will reject invalid or non-existent agent identifiers."),

(["already listed", "duplicate listing"],
 "Systems prevent duplicate listings of the same property to maintain consistency."),

(["remove listing not working", "cannot remove listing"],
 "Removing a listing may fail if the user is not the owner or if the listing does not exist."),

# ================= SEARCH =================
(["search not working", "no properties found"],
 "Search results depend on filters like type, sector, and budget. If nothing appears, it usually means no records match all conditions."),

(["filter mismatch", "wrong search results"],
 "Incorrect or overly strict filters can lead to no results or unexpected matches."),

# ================= SYSTEM / GENERAL =================
(["program crash", "app closing", "system crash"],
 "Crashes are often caused by invalid inputs, missing files, or unexpected data formats. Ensuring valid input and complete data helps prevent this."),

(["invalid input", "wrong format"],
 "Many systems expect inputs in a strict format. Even small deviations can cause commands to fail."),

(["slow performance", "program lag"],
 "Performance issues may arise from repeated file access, large data sets, or inefficient processing logic."),

(["unexpected behavior", "wrong output"],
 "Unexpected results often occur due to data inconsistencies, incorrect assumptions, or edge cases not handled properly."),

# ================= EDGE CASES =================
(["zero value", "0 amount issue"],
 "Zero values are often treated as invalid in financial operations and may cause operations to be skipped."),

(["rounding issue", "decimal problem"],
 "Floating point values can sometimes lead to rounding differences, especially in financial calculations."),

(["multiple operations fail", "random errors"],
 "If multiple features fail, the root cause is often shared—such as corrupted data or a missing dependency."),

]