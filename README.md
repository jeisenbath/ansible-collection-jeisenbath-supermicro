# Ansible Collection - jeisenbath.supermicro

Documentation for the collection.

## Included Content

<!--start collection content-->
### Roles
| Name                                    | Description              |
|-----------------------------------------|--------------------------|
| jeisenbath.supermicro.accounts          | Configure accounts       |
| jeisenbath.supermicro.bios              | Configure bios settings  |
| jeisenbath.supermicro.interfaces        | Configure interfaces     |
| jeisenbath.supermicro.managers          | Configure timezone       |
| jeisenbath.supermicro.network_protocols | Configure NTP, SNMP, SSH |

### Installing the Collection from Ansible Galaxy

Before using this collection, you need to install it with the Ansible Galaxy command-line tool:
```bash
ansible-galaxy collection install git+https://github.com/jeisenbath/ansible-collection-jeisenbath-supermicro.git
```

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:
```yaml
---
collections:
  - name: jeisenbath.supermicro
    type: git
    source: https://github.com/jeisenbath/ansible-collection-jeisenbath-supermicro
```

Note that if you install the collection from Ansible Galaxy, it will not be upgraded automatically when you upgrade the `ansible` package. To upgrade the collection to the latest available version, run the following command:
```bash
ansible-galaxy collection install git+https://github.com/jeisenbath/ansible-collection-jeisenbath-supermicro.git --upgrade
```

You can also install a specific version of the collection, for example, if you need to downgrade when something is broken in the latest version (please report an issue in this repository). Use the following syntax to install version `1.0.0`:

```bash
ansible-galaxy collection install git+https://github.com/jeisenbath/ansible-collection-jeisenbath-supermicro.git,v1.0.0
```

See [Ansible Using collections](https://docs.ansible.com/ansible/devel/user_guide/collections_using.html) for more details.

## Licensing

<!-- Include the appropriate license information here and a pointer to the full licensing details. If the collection contains modules migrated from the ansible/ansible repo, you must use the same license that existed in the ansible/ansible repo. See the GNU license example below. -->

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.

## Community Code of Conduct

Please see the official [Ansible Community Code of Conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html#code-of-conduct).
