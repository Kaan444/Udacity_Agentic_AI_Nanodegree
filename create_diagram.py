import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.lines as mlines

# Create figure and axis
fig, ax = plt.subplots(1, 1, figsize=(16, 14))
ax.set_xlim(0, 16)
ax.set_ylim(0, 14)
ax.axis('off')

# Color scheme
COLOR_CUSTOMER = '#FFE5E5'
COLOR_ORCHESTRATOR = '#E3F2FD'
COLOR_AGENT = '#FFF9C4'
COLOR_TOOL = '#E8F5E9'
COLOR_DB = '#F3E5F5'

def draw_box(ax, x, y, width, height, text, color, fontsize=9, fontweight='normal'):
    """Draw a rounded rectangle box with text"""
    box = FancyBboxPatch(
        (x - width/2, y - height/2), width, height,
        boxstyle="round,pad=0.1",
        edgecolor='black',
        facecolor=color,
        linewidth=1.5
    )
    ax.add_patch(box)
    ax.text(x, y, text, ha='center', va='center', fontsize=fontsize,
            fontweight=fontweight, wrap=True)

def draw_arrow(ax, x1, y1, x2, y2, label='', style='->'):
    """Draw an arrow between two points"""
    arrow = FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle=style,
        color='black',
        linewidth=1.5,
        mutation_scale=20
    )
    ax.add_patch(arrow)
    if label:
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        ax.text(mid_x + 0.2, mid_y, label, fontsize=7, style='italic',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

# Title
ax.text(8, 13.5, 'Munder Difflin Multi-Agent System Architecture',
        ha='center', fontsize=16, fontweight='bold')

# Customer Request (Top)
draw_box(ax, 8, 12.5, 3, 0.6, 'Customer Request\n(includes Date)', COLOR_CUSTOMER, 10, 'bold')

# Orchestrator Agent (Central hub)
draw_box(ax, 8, 10.5, 3.5, 0.8, 'Orchestrator Agent', COLOR_ORCHESTRATOR, 11, 'bold')

# Arrow from Customer to Orchestrator
draw_arrow(ax, 8, 12.2, 8, 11.3)

# Orchestrator's direct tools (top row)
orch_tools_y = 9
draw_box(ax, 10.5, orch_tools_y, 2.0, 0.5, 'get_item_catalog_tool\n(SQL SELECT inventory)', COLOR_TOOL, 7)
draw_box(ax, 13, orch_tools_y, 2.0, 0.5, 'search_quote_history_tool\n(search_quote_history)', COLOR_TOOL, 7)
draw_box(ax, 15.2, orch_tools_y, 2.0, 0.5, 'generate_financial_report_tool\n(internal reporting only)', COLOR_TOOL, 7)

# Arrows from Orchestrator to its tools
draw_arrow(ax, 9.2, 10.2, 9.6, 9.25)
draw_arrow(ax, 9.5, 10.1, 12.1, 9.25)
draw_arrow(ax, 9.7, 10.0, 14.3, 9.25)

# Agent wrapper tools (middle row)
wrapper_y = 7.5
draw_box(ax, 3, wrapper_y, 2.4, 0.6, 'ask_inventory_agent\n(delegates)', COLOR_TOOL, 8, 'bold')
draw_box(ax, 8, wrapper_y, 2.4, 0.6, 'ask_quote_agent\n(delegates)', COLOR_TOOL, 8, 'bold')
draw_box(ax, 13, wrapper_y, 2.4, 0.6, 'ask_fulfillment_agent\n(delegates)', COLOR_TOOL, 8, 'bold')

# Arrows from Orchestrator to wrapper tools
draw_arrow(ax, 6.5, 10.3, 3.8, 8.1)
draw_arrow(ax, 8, 10.1, 8, 8.1)
draw_arrow(ax, 9.5, 10.3, 12.2, 8.1)

# Actual Agents (lower row)
agent_y = 5.8
draw_box(ax, 3, agent_y, 2.2, 0.7, 'InventoryAgent', COLOR_AGENT, 10, 'bold')
draw_box(ax, 8, agent_y, 2.2, 0.7, 'QuoteAgent', COLOR_AGENT, 10, 'bold')
draw_box(ax, 13, agent_y, 2.2, 0.7, 'FulfillmentAgent', COLOR_AGENT, 10, 'bold')

# Arrows from wrapper tools to agents
draw_arrow(ax, 3, 7.2, 3, 6.15)
draw_arrow(ax, 8, 7.2, 8, 6.15)
draw_arrow(ax, 13, 7.2, 13, 6.15)

# InventoryAgent tools
inv_tools_y = 4
inv_tools = [
    'safe_inventory_status_tool\n(availability check)',
    'get_item_catalog_tool\n(SQL SELECT inventory)',
    'get_all_inventory_tool\n(get_all_inventory)',
    'get_stock_level_tool\n(get_stock_level)',
    'create_stock_order_tool\n(create_transaction:\nstock_orders)'
]
for i, tool in enumerate(inv_tools):
    x_pos = 0.5 + i * 1.1
    draw_box(ax, x_pos, inv_tools_y, 1.0, 0.7, tool, COLOR_TOOL, 6)
    draw_arrow(ax, 3, 5.45, x_pos, 4.35)

# QuoteAgent tools
quote_tools_y = 4
quote_tools = [
    'search_quote_history_tool\n(search_quote_history)',
    'get_item_catalog_tool\n(SQL SELECT inventory)'
]
for i, tool in enumerate(quote_tools):
    x_pos = 7 + i * 2
    draw_box(ax, x_pos, quote_tools_y, 1.8, 0.5, tool, COLOR_TOOL, 6)
    draw_arrow(ax, 8, 5.45, x_pos, 4.25)

# FulfillmentAgent tools
ful_tools_y = 4
ful_tools = [
    'safe_inventory_status_tool\n(availability check)',
    'create_sale_tool\n(create_transaction:\nsales)',
    'supplier_delivery_date_tool\n(get_supplier_delivery_date)'
]
for i, tool in enumerate(ful_tools):
    x_pos = 11.5 + i * 1.5
    draw_box(ax, x_pos, ful_tools_y, 1.3, 0.7, tool, COLOR_TOOL, 6)
    draw_arrow(ax, 13, 5.45, x_pos, 4.35)

# Database (bottom)
db_y = 1.5
draw_box(ax, 8, db_y, 3, 0.8, 'SQLite Database\nmunder_difflin.db\n(inventory, transactions, quotes, quote_requests)',
         COLOR_DB, 9, 'bold')

# Arrows from all tools to database (simplified - just a few representative ones)
# From inventory tools
draw_arrow(ax, 1, 3.65, 6.5, 1.9, style='->')
draw_arrow(ax, 3, 3.65, 7.5, 1.9, style='->')

# From quote tools
draw_arrow(ax, 7, 3.75, 7.5, 1.9, style='->')
draw_arrow(ax, 9, 3.75, 8.5, 1.9, style='->')

# From fulfillment tools
draw_arrow(ax, 12, 3.65, 8.5, 1.9, style='->')
draw_arrow(ax, 14, 3.65, 9.0, 1.9, style='->')

# Legend
legend_y = 0.5
legend_elements = [
    patches.Patch(facecolor=COLOR_CUSTOMER, edgecolor='black', label='Customer Input'),
    patches.Patch(facecolor=COLOR_ORCHESTRATOR, edgecolor='black', label='Orchestrator'),
    patches.Patch(facecolor=COLOR_AGENT, edgecolor='black', label='Specialist Agent'),
    patches.Patch(facecolor=COLOR_TOOL, edgecolor='black', label='Tool/Function'),
    patches.Patch(facecolor=COLOR_DB, edgecolor='black', label='Database')
]
ax.legend(handles=legend_elements, loc='lower center', ncol=5,
          frameon=True, fontsize=9, bbox_to_anchor=(0.5, -0.05))

# Add notes box
notes_text = """Key Design Principles:
• Text-only communication between agents
• Privacy-safe: No inventory counts/cash exposed to customers
• Orchestrator delegates via wrapper tools
• Specialist agents use domain-specific tools
• All transactions logged to SQLite database"""

ax.text(0.5, 11.5, notes_text, fontsize=8,
        bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', alpha=0.8),
        verticalalignment='top', family='monospace')

plt.tight_layout()
plt.savefig('/Users/ihsanmutlu/Desktop/git-hub/Udacity_Agentic_AI_Nanodegree/architecture_diagram.png',
            dpi=300, bbox_inches='tight', facecolor='white')
print("Diagram saved as: architecture_diagram.png")
plt.close()
