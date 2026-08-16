import { useState } from 'react';
import { createClient } from 'genlayer-js';

const CONTRACT_ADDRESS = "0xGenLayerDeployedContractAddress";

export default function App() {
  const [url, setUrl] = useState('');
  const [state, setState] = useState('');
  const [loading, setLoading] = useState(false);

  const client = createClient({ network: 'genlayer-testnet' });

  // Real client WRITE path to the contract
  const handleWriteVerify = async () => {
    setLoading(true);
    try {
      const tx = await client.writeContract({
        address: CONTRACT_ADDRESS,
        functionName: 'verify_authoritative_source',
        args: [url],
      });
      await tx.wait();
      handleReadState();
    } catch (error) {
      console.error("Write transaction error:", error);
    } finally {
      setLoading(false);
    }
  };

  // Real client READ path from the contract
  const handleReadState = async () => {
    const currentStatus = await client.readContract({
      address: CONTRACT_ADDRESS,
      functionName: 'read_verification_state',
      args: [url],
    });
    setState(currentStatus);
  };

  return (
    <div style={{ padding: '30px', fontFamily: 'sans-serif' }}>
      <h2>Authoritative Data Verifier DApp</h2>
      <input 
        type="text" 
        value={url} 
        onChange={(e) => setUrl(e.target.value)} 
        placeholder="Enter live web source URL" 
        style={{ width: '380px', padding: '8px' }}
      />
      <button onClick={handleWriteVerify} disabled={loading} style={{ padding: '8px 16px', marginLeft: '10px' }}>
        {loading ? "Processing..." : "Verify via Contract"}
      </button>

      {state && (
        <div style={{ marginTop: '15px' }}>
          <strong>Contract Verification State:</strong> {state}
        </div>
      )}
    </div>
  );
}
